import json
from pyproj            import Transformer

from django.db.models  import Q
from django.views      import View
from django.http       import JsonResponse

from ..models          import Room, TradeType

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
        dong_code  = request.GET.get('dongCode')
        q          = Q()

        if len(locations) == 2 and \
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