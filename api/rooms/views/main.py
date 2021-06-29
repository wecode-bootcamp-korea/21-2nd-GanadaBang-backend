import requests, json

from django.views     import View
from django.http      import JsonResponse

from my_settings import SEARCH_API_KEY

class SearchRoomView(View):
    def get(self, request):
        address  = request.GET.get('address')
        type     = request.GET.get('type')
        category = request.GET.get('category')
        
        if len(address) < 2 : 
            return JsonResponse({'message':'ADDRESS_IS_TOO_SHORT'}, status=400)

        VWORLD_URL = (f'http://api.vworld.kr/req/search?service=search&request=search&version=2.0&crs=EPSG:4326&size=100&page=1&query={address}&type={type}&category={category}&format=json&errorformat=json&key={SEARCH_API_KEY}')
        response   = requests.get(VWORLD_URL, timeout=10).json()

        if not response['response']['status'] == 'OK':
            return JsonResponse({'message':'VALUE_ERROR'}, status= 400)
    
        return JsonResponse({'address':response['response']['result']['items']}, status=200) 