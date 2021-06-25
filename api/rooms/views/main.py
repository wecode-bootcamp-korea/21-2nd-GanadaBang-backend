import requests, json

from django.views     import View
from django.http      import JsonResponse

from ..models import Room
from my_settings import SEARCH_API_KEY

class SearchRoomView(View):
    def get(self, request):
        address  = request.GET.get('address')
        type     = request.GET.get('type')
        category = request.GET.get('category')
        
        if len(address) < 2 : 
            return JsonResponse({'message':'ADDRESS_IS_TOO_SHORT'}, status=400)

        VWORLD_URL = f'http://api.vworld.kr/req/search?service=search&request=search&version=2.0&crs=EPSG:4326&size=100&page=1&query={address}&type={type}&category={category}&format=json&errorformat=json&key={SEARCH_API_KEY}'
        response   = requests.get(VWORLD_URL, timeout=10).json()

        if not response['response']['status'] == 'OK':
            return JsonResponse({'message':'VALUE_ERROR'}, status= 400)
    
        return JsonResponse({'address':response['response']['result']['items']}, status=200) 

class RoomSuggestionView(View):
    def get(self, request):
            keyword_sort = request.GET.get('keyword_sort')
            offset       = int(request.GET.get('offset', 0))
            limit        = int(request.GET.get('limit', 1))
            
            rooms = Room.objects.select_related('location','room_type','trade_type')\
                    .filter(location__dong__icontains=keyword_sort)\
                    .prefetch_related('roomimage_set')\
                    .order_by('?')[offset:offset+limit]

            result =[{
                'id'          : room.id,
                'title'       : room.title,
                'content'     : room.content,
                'floor'       : room.floor,
                'room_count'  : room.room_count,
                'room_area'   : room.room_area,
                'deposit'     : room.deposit,
                'monthly_rent': room.monthly_rent,
                'sale'        : room.sale,
                'room_type'   : room.room_type.name,
                'trade_type'  : room.trade_type.name,
                'room_image'  : room.roomimage_set.all()[0].url,
                'state'       : room.location.state,
                'city'        : room.location.city,
                'dong'        : room.location.dong,
                'dong_code'   : room.location.dong_code
            } for room in rooms]
            
            return JsonResponse({'result':result}, status=200)