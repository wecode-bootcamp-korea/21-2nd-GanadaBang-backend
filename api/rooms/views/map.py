import json, requests, uuid, boto3
from pyproj                          import Transformer

from json.decoder                    import JSONDecodeError
from django.db.models.expressions    import Value
from django.db.models.functions.text import Concat

from django.db                       import transaction
from django.db.models                import Q, Count, F
from django.db.models.functions      import Left
from django.views                    import View
from django.http                     import JsonResponse

from ..models                        import Location, Room, RoomImage, RoomType, TradeType
from ganadabang.settings             import SEARCH_API_KEY, AWS_S3_ACCESS_KEY_ID, \
                                            AWS_S3_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, \
                                            AWS_S3_UPLOAD_URL

def parse_wgs84_to_utmk(longitude, latitude):
    return Transformer.from_crs("epsg:4326", "epsg:5178").transform(latitude, longitude)

def parse_utmk_to_wgs84(utmk_x, utmk_y):
    return Transformer.from_crs("epsg:5178", "epsg:4326").transform(utmk_x, utmk_y)

def upload_file_to_aws(files):
    s3 = boto3.client(
        's3',
        aws_access_key_id     = AWS_S3_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_S3_SECRET_ACCESS_KEY
    )
    
    file_urls = []

    for file in files:
        uuid_name = str(uuid.uuid4()).replace('-','')
        s3.upload_fileobj(
            file,
            AWS_STORAGE_BUCKET_NAME,
            uuid_name+file.name,
            ExtraArgs = {
                    "ContentType" : file.content_type
                }
        )
        file_urls.append(f'{AWS_S3_UPLOAD_URL}/{uuid_name+file.name}')
    
    return file_urls

class FakeRoomData:
    def __init__(self, request):
        self.request = request

    def parse_data(self):
        data = json.loads(self.request.POST['data'])
        return {
            'address'        : data['address'],
            'detail'         : data['detail'],
            'title'          : data.get('title', '방1'),
            'content'        : data.get('content', '방1입니다'),
            'room_type'      : int(data.get('room_type', RoomType.Enum.ONE_ROOM.value)),
            'trade_type'     : int(data.get('trade_type', TradeType.Enum.DEPOSIT.value)),
            'monthly_rent'   : int(data.get('monthly_rent', 0)),
            'deposit'        : int(data.get('deposit', 123450000)),
            'sale'           : int(data.get('sale', 0)),
            'agent'          : data.get('agent', '가나다방 공식 부동산'),
            'floor'          : int(data.get('floor', 5)),
            'room_area'      : float(data.get('room_area', 148.760331)),
            'room_count'     : int(data.get('room_count', 5)),
            'bathroom_count' : int(data.get('bathroom_count', 3)),
            'heating_type'   : data.get('heating_type', '유'),
            'elevator'       : data.get('elevator', '유'),
            'room_options'   : data.get('room_options', [1,2,3])
        }

def room_filter(func):
    def wrapper(self, request, *args, **kwargs):
        filters     = json.loads(request.GET.get('filter', '{}'))
        room_types  = filters.get('roomType', [])
        trade_types = filters.get('tradeType', [])
        locations   = json.loads(request.GET.get('location', '[]'))
        dong_code   = request.GET.get('code')
        q           = Q()

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
            q &= Q(location__dong_code__istartswith=dong_code)

        request.q = q
        return func(self,request, *args, **kwargs)

    return wrapper

class RoomListView(View):
    @room_filter
    def get(self, request):
        offset = int(request.GET.get('offset', -1))
        limit  = int(request.GET.get('limit', 15))

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
                'deposit'      : room.deposit,
                'monthly_rent' : room.monthly_rent,
                'sale'         : room.sale,
                'room_type'    : room.room_type.name,
                'trade_type'   : room.trade_type.name,
                'room_image'   : room.roomimage_set.all()[0].url,
                'state'        : room.location.state,
                'city'         : room.location.city,
                'dong'         : room.location.dong,
                'location'     : {
                    'lng' : float(room.location.longitude),
                    'lat' : float(room.location.latitude)
                    }
            } for room in rooms]
        }

        return JsonResponse(result, status=200)

    def post(self, request):
        try:
            fake_data = FakeRoomData(request)
            room_data = fake_data.parse_data()
            address   = room_data['address']
            detail    = room_data['detail']

            response = requests.get('http://api.vworld.kr/req/address',
            {
                'key'     : SEARCH_API_KEY,
                'service' : 'address',
                'request' : 'getcoord',
                'version' : '2.0',
                'crs'     : 'EPSG:4326',
                'format'  : 'json',
                'type'    : 'PARCEL',
                'refine'  : 'false',
                'simple'  : True,
                'address' : address + ' ' + detail
            },  timeout=10).json()

            lng = response['response']['result']['point']['x']
            lat = response['response']['result']['point']['y']

            utmk = parse_wgs84_to_utmk(lng, lat)

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
                'category'    : 'L4',
                'query'       : address
            },  timeout=10).json()

            code = response['response']['result']['items'][0]['id']

            with transaction.atomic():
                location = Location.objects.create(
                    state     = address.split(' ')[0],
                    city      = ' '.join(address.split(' ')[1:-1]),
                    dong      = address.split(' ')[-1],
                    dong_code = code,
                    latitude  = lat,
                    longitude = lng,
                    utmk_x    = utmk[0],
                    utmk_y    = utmk[1]
                )

                room = Room.objects.create(
                    title          = room_data['title'],
                    content        = room_data['content'],
                    location_id    = location.id,
                    room_type_id   = room_data['room_type'],
                    trade_type_id  = room_data['trade_type'],
                    monthly_rent   = room_data['monthly_rent'],
                    deposit        = room_data['deposit'],
                    sale           = room_data['sale'],
                    agent          = room_data['agent'],
                    floor          = room_data['floor'],
                    room_area      = room_data['room_area'],
                    room_count     = room_data['room_count'],
                    bathroom_count = room_data['bathroom_count'],
                    heating_type   = room_data['heating_type'],
                    elevator       = room_data['elevator']
                )

                for option in room_data['room_options'] :
                    room.option.add(option)

                files     = request.FILES.getlist('files')
                file_urls = upload_file_to_aws(files)

                if len(files) == 0:
                    transaction.set_rollback(True)
                    return JsonResponse({'message':'NO_IMAGES'}, status=400)

                roomImages = [
                    RoomImage(room_id = room.id, url=url) 
                    for url in file_urls]

                RoomImage.objects.bulk_create(roomImages)

            return JsonResponse({'message':'CREATED'}, status=201)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

        except JSONDecodeError:
            return JsonResponse({'message':'INVALID_VALUE'}, status=400)

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