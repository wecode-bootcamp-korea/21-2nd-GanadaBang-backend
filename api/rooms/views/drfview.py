
import requests
from rest_framework import viewsets

from rest_framework.viewsets import ModelViewSet
from rest_framework          import serializers, status, generics
from rest_framework.views    import APIView
from rest_framework.response import Response
from rest_framework.filters  import SearchFilter, OrderingFilter

from .map          import room_filter
from ..serializers import RoomSerializer
from ..models      import Room
from my_settings   import SEARCH_API_KEY

class RoomRandomAPI:
    def __init__(self, keyword_sort, offset, limit):
        self.keyword_sort = keyword_sort
        self.offset       = offset
        self.limit        = limit

    def get_room(self): 
        rooms = Room.objects.filter(location__detail__icontains=self.keyword_sort)\
                .order_by('?')[self.offset:self.offset+self.limit]
        serializer = RoomSerializer(rooms, many=True)
        return serializer
    
class RoomSearchAPIView(APIView):
    def get(self, request):
        roomrandom_api = RoomRandomAPI(
            keyword_sort = request.GET.get('keyword_sort'),
            offset       = int(request.GET.get('offset', 0)),
            limit        = int(request.GET.get('limit', 1)),
        )
        result_random = roomrandom_api.get_room()
        return Response(result_random.data, status=status.HTTP_200_OK)


# class RoomSearchAPIView(APIView):
#     def get(self, request):
#         keyword_sort = request.GET.get('keyword_sort')
#         offset       = int(request.GET.get('offset', 0))
#         limit        = int(request.GET.get('limit', 1))
        
#         rooms = Room.objects.filter(location__detail__icontains=keyword_sort)\
#                 .order_by('?')[offset:offset+limit]
#         serializer = RoomSerializer(rooms, many=True)
#         return Response(serializer.data)
    

class VworldAPI:
    def __init__(self, address, type, category, api_key):
        self.address  = address
        self.type     = type
        self.category = category
        self.api_key  = api_key
        
    def get_address(self):
        VWORLD_URL = f'http://api.vworld.kr/req/search?service=search&request=search&version=2.0&crs=EPSG:4326&size=100&page=1&query={self.address}&type={self.type}&category={self.category}&format=json&errorformat=json&key={self.api_key}'            
        response   = requests.get(VWORLD_URL, timeout=10).json()
        if len(self.address) < 2 : 
            return Response({'message':'ADDRESS_IS_TOO_SHORT'}, status=status.HTTP_400_BAD_REQUEST)
        if not response['response']['status'] == 'OK':
            return Response({'message':'VALUE_ERROR'}, status=status.HTTP_400_BAD_REQUEST)
        return response['response']['result']['items']
    

class AddressSearchAPIView(APIView):
    def get(self, request):
        vworld_api = VworldAPI(
            address  = request.GET.get('address'),
            type     = request.GET.get('type'),
            category = request.GET.get('category'),
            api_key  = SEARCH_API_KEY
        )
        result_address = vworld_api.get_address()
        return Response(result_address, status=status.HTTP_200_OK)


# class AddressSearchAPIView(APIView):
    # def get(self, request):
    #     address  = request.GET.get('address')
    #     type     = request.GET.get('type')
    #     category = request.GET.get('category')
        
    #     if len(address) < 2 : 
    #         return Response({'message':'ADDRESS_IS_TOO_SHORT'}, status=status.HTTP_400_BAD_REQUEST)
    
    #     VWORLD_URL = f'http://api.vworld.kr/req/search?service=search&request=search&version=2.0&crs=EPSG:4326&size=100&page=1&query={address}&type={type}&category={category}&format=json&errorformat=json&key={SEARCH_API_KEY}'
    #     response   = requests.get(VWORLD_URL, timeout=10).json()
        
    #     if not response['response']['status'] == 'OK':
    #         return Response({'message':'VALUE_ERROR'}, status=status.HTTP_400_BAD_REQUEST)
    #     return Response({'address':response['response']['result']['items']}, status=status.HTTP_200_OK) 









# class FakeRoomData:
#     def __init__(self, request):
#         self.request = request

#     def parse_data(self):
#         data = json.loads(self.request.POST['data'])
#         return {
#             'address'        : data['address'],
#             'detail'         : data['detail'],
#             'title'          : data.get('title', '방1'),
#             'content'        : data.get('content', '방1입니다'),
#             'room_type'      : int(data.get('room_type', RoomType.Enum.ONE_ROOM.value)),
#             'trade_type'     : int(data.get('trade_type', TradeType.Enum.DEPOSIT.value)),
#             'monthly_rent'   : int(data.get('monthly_rent', 0)),
#             'deposit'        : int(data.get('deposit', 123450000)),
#             'sale'           : int(data.get('sale', 0)),
#             'agent'          : data.get('agent', '가나다방 공식 부동산'),
#             'floor'          : int(data.get('floor', 5)),
#             'room_area'      : float(data.get('room_area', 148.760331)),
#             'room_count'     : int(data.get('room_count', 5)),
#             'bathroom_count' : int(data.get('bathroom_count', 3)),
#             'heating_type'   : data.get('heating_type', '유'),
#             'elevator'       : data.get('elevator', '유'),
#             'room_options'   : data.get('room_options', [1,2,3])
#         }
    
def post(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class UploadRoomAPIView(APIView):    
     def post(self, request):
            serializer = RoomSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
            
        #     address = serializer.data['address']
        #     detail= serializer.data['detail']
        #     title = serializer.data['title']
        #     content = serializer.data['content']
        #     room_type = serializer.data['room_type']
        #     trade_type = serializer.data['rade_type']
        #     monthly_rent = serializer.data['monthly_rent']
        #     deposit = serializer.data['deposit']
        #     sale = serializer.data['sale']
        #     agent = serializer.data['agent']
        #     floor = serializer.data['floor']
        #     room_area=serializer.data['room_area']
        #     room_count =serializer.data['room_count']
        #     bathroom_count = serializer.data['bathroom_count']
        #     heating_type= serializer.data['heating_type']
        #     elevator=serializer.data['elevator'] 
        #     room_options = serializer.data['room_options']
            
        #     room = Room.objects.create(
        #             title          = room_data['title'],
        #             content        = room_data['content'],
        #             location_id    = location.id,
        #             room_type_id   = room_data['room_type'],
        #             trade_type_id  = room_data['trade_type'],
        #             monthly_rent   = room_data['monthly_rent'],
        #             deposit        = room_data['deposit'],
        #             sale           = room_data['sale'],
        #             agent          = room_data['agent'],
        #             floor          = room_data['floor'],
        #             room_area      = room_data['room_area'],
        #             room_count     = room_data['room_count'],
        #             bathroom_count = room_data['bathroom_count'],
        #             heating_type   = room_data['heating_type'],
        #             elevator       = room_data['elevator']
        #         )

        #         for option in room_data['room_options'] :
        #             room.option.add(option)

        #         files     = request.FILES.getlist('files')
        #         file_urls = upload_file_to_aws(files)

        #         if len(files) == 0:
        #             transaction.set_rollback(True)
        #             return JsonResponse({'message':'NO_IMAGES'}, status=400)

        #         roomImages = [
        #             RoomImage(room_id = room.id, url=url) 
        #             for url in file_urls]

        #         RoomImage.objects.bulk_create(roomImages)

        #     return JsonResponse({'message':'CREATED'}, status=201)

        # except KeyError:
        #     return JsonResponse({'message':'KEY_ERROR'}, status=400)

        # except JSONDecodeError:
        #     return JsonResponse({'message':'INVALID_VALUE'}, status=400)

class PostViewSet(viewsets.ModelViewSet):
        queryset = Room.objects.all()
        serializer_class = RoomSerializer
    


class RoomAPIView(APIView):   
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data) 
    
    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RoomDetailAPIView(APIView):
    def get(self, request, pk):
        room = Room.objects.get(pk=pk)
        serializer = RoomSerializer(room)
        return Response(serializer.data)
    
    def put(self, request, pk):
        room = Room.objects.get(pk=pk)
        serializer = RoomSerializer(room, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class GroupaddressAPIView(APIView):
    
#     @room_filter
#     def get(self, request): 

#         zoom = int(request.GET.get('zoom', 13))

#         if zoom <= 9 :
#             category = 'L1'
#             value    = {'name'  : F('location__state'), 'code' : Left('location__dong_code', 2)}
#             annotate = {'count' : Count('code'), 'address' : F('location__state')}
        
#         elif zoom <= 12:
#             category = 'L2'
#             value    = {'name' : F('location__city'), 'code' : Left('location__dong_code', 5)}
#             annotate = {
#                 'count'   : Count('code'),
#                 'address' : Concat('location__state', Value(' '), 'location__city')
#             }
        
#         else:
#             category = 'L4'
#             value    = {'name' : F('location__dong'), 'code' : F('location__dong_code')}
#             annotate = {
#                 'count'   : Count('code'),
#                 'address' : Concat('location__state', Value(' '), 'location__city', Value(' '), 'location__dong')
#             }

#         rooms = Room.objects.select_related('location').values(**value).filter(request.q).annotate(**annotate)

#         markers = []
#         for room in rooms:
#             response = requests.get('http://api.vworld.kr/req/search',
#             {
#                 'key'         : SEARCH_API_KEY,
#                 'service'     : 'search',
#                 'request'     : 'search',
#                 'version'     : '2.0',
#                 'crs'         : 'EPSG:4326',
#                 'size'        : 1000,
#                 'offset'      : 0,
#                 'limit'       : 1,
#                 'type'        : 'district',
#                 'format'      : 'json',
#                 'errorformat' : 'json',
#                 'category'    : category,
#                 'query'       : room['address']
#             },  timeout=10).json()

#             markers.append(
#                 {
#                     'name' : room['name'],
#                     'count': room['count'],
#                     'code' : response['response']['result']['items'][0]['id'],
#                     'lng'  : response['response']['result']['items'][0]['point']['x'],
#                     'lat'  : response['response']['result']['items'][0]['point']['y']
#                 }
#             )

#         result = {
#             'markers' : markers
#         }

#         return JsonResponse(result, status=200)
    