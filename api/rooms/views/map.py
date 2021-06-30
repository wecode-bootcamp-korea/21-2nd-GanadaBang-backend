import json, requests
from django.db.models.expressions import Value
from django.db.models.functions.text import Concat
from pyproj                     import Transformer

from django.db.models           import Q, Count, F
from django.db.models.functions import Left
from django.views               import View
from django.http                import JsonResponse

from ..models                   import Room, TradeType
from ganadabang.settings        import SEARCH_API_KEY

def parse_wgs84_to_utmk(longitude, latitude):
    return Transformer.from_crs("epsg:4326", "epsg:5178").transform(latitude, longitude)

def parse_utmk_to_wgs84(utmk_x, utmk_y):
    return Transformer.from_crs("epsg:5178", "epsg:4326").transform(utmk_x, utmk_y)

def room_filter(func):
    def wrapper(self, request, *args, **kwargs):
        filters = json.loads(request.GET.get('filter', '{}'))
        room_types  = filters.get('roomType', [])
        trade_types = filters.get('tradeType', [])
        locations  = json.loads(request.GET.get('location', '[]'))
        dong_code  = request.GET.get('code')
        q          = Q()

        if not dong_code and len(locations) == 2 and \
            len(locations[0]) == 2 and len(locations[1]) == 2:
            sw = parse_wgs84_to_utmk(locations[0][0], locations[0][1])
            ne = parse_wgs84_to_utmk(locations[1][0], locations[1][1])

            q &= Q(location__utmk_x__range = [sw[0], ne[0]], 
                location__utmk_y__range = [sw[1], ne[1]])

        if trade_types:
            trade_q      = Q()
            deposit      = filters.get('deposit', [0, 999999999])
            monthly_rent = filters.get('monthlyRent', [0, 999999999])
            sale         = filters.get('sale', [0, 999999999])
            
            if TradeType.Enum.MONTHLY_RENT.value in trade_types :
                trade_q |= Q(
                    trade_type_id=TradeType.Enum.MONTHLY_RENT.value, 
                    monthly_rent__range=monthly_rent, deposit__range=deposit)

            if TradeType.Enum.DEPOSIT.value in trade_types :
                trade_q |= Q(trade_type_id=TradeType.Enum.DEPOSIT.value, 
                    deposit__range=deposit)

            if TradeType.Enum.SALE.value in trade_types :
                trade_q |= Q(trade_type_id=TradeType.Enum.SALE.value,
                    sale__range=sale)

            q &= Q(trade_q)

        if room_types:
            q &= Q(room_type_id__in=room_types)

        if dong_code:
            q &= Q(location__dong_code=dong_code)

        request.q = q
        return func(self,request, *args, **kwargs)

    return wrapper

class RoomListView(View):
    @room_filter
    def get(self, request):
        offset    = int(request.GET.get('offset', 0))
        limit     = int(request.GET.get('limit', 15))

        rooms = Room.objects \
            .select_related('location', 'room_type', 'trade_type') \
            .prefetch_related('roomimage_set').filter(request.q)

        total_count = rooms.count()

        if offset >= 0 and limit > 0:
            rooms    = rooms[offset:offset+limit]
            has_more = limit <= total_count

        result = {
            'total'     : total_count,
            'offset'    : offset,
            'limit'     : limit,
            'room_list' : [{
                'id'           : room.id,
                'title'        : room.title,
                'content'      : room.content,
                'floor'        : room.floor,
                'room_count'   : room.room_count,
                'room_area'    : room.room_area,
                'desposit'     : room.deposit,
                'monthly_rent' : room.monthly_rent,
                'sale'         : room.sale,
                'room_type'    : room.room_type.name,
                'trade_type'   : room.trade_type.name,
                'room_image'   : room.roomimage_set.all()[0].url,
                'state'        : room.location.state,
                'city'         : room.location.city,
                'dong'         : room.location.dong,
                'location'     : {
                    'x' : float(room.location.longitude),
                    'y' : float(room.location.latitude)
                    }
            } for room in rooms]
        }

        return JsonResponse(result, status=200)

class RoomGroupView(View):
    @room_filter
    def get(self, request): 

        zoom = int(request.GET.get('zoom', 13))

        if zoom <= 9 :
            category = 'L1'
            value    = {'name'  : F('location__state'), 'code' : Left('location__dong_code', 2)}
            annotate = {'count' : Count('code'), 'address' : F('location__state')}
        
        elif zoom <= 12:
            category = 'L2'
            value    = {'name' : F('location__city'), 'code' : Left('location__dong_code', 5)}
            annotate = {
                'count'   : Count('code'),
                'address' : Concat('location__state', Value(' '), 'location__city')
            }
        
        else:
            category = 'L4'
            value    = {'name' : F('location__dong'), 'code' : F('location__dong_code')}
            annotate = {
                'count'   : Count('code'),
                'address' : Concat('location__state', Value(' '), 'location__city', Value(' '), 'location__dong')
            }

        rooms = Room.objects.select_related('location').values(**value).filter(request.q).annotate(**annotate)

        markers = []
        for room in rooms:

            response = requests.get('http://api.vworld.kr/req/search',
            {
                'key'         : SEARCH_API_KEY,
                'service'     : 'search',
                'request'     : 'search',
                'version'     : '2.0',
                'crs'         : 'EPSG:4326',
                'size'        : 1000,
                'offset'      : 0,
                'limit'       : 1,
                'type'        : 'district',
                'format'      : 'json',
                'errorformat' : 'json',
                'category'    : category,
                'query'       : room['address']
            },  timeout=10).json()

            markers.append(
                {
                    'name' : room['name'],
                    'count': room['count'],
                    'code' : response['response']['result']['items'][0]['id'],
                    'lng'  : response['response']['result']['items'][0]['point']['x'],
                    'lat'  : response['response']['result']['items'][0]['point']['y']
                }
            )

        result = {
            'markers' : markers
        }

        return JsonResponse(result, status=200)