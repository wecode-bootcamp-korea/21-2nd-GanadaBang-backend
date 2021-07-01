import json, jwt, requests

from django.views        import View
from django.http         import JsonResponse
from django.db.utils     import IntegrityError

from ganadabang.settings import SECRET_KEY, ALGORITHM
from .models             import User

class KakaoAPI:
    def __init__(self, access_token):
        self.access_token = access_token

    def get_kakao_user(self):
        headers       = ({'Authorization' : f'Bearer {self.access_token}'})
        kakao_url     = 'https://kapi.kakao.com/v2/user/me'
        response      = requests.get(kakao_url, headers = headers, timeout=5)
        
        if not response.status_code == 200:
            return JsonResponse({'message' : 'INVALID_TOKEN'}, status=400)

        return response.json()

class KakaoSigninView(View):
    def post(self,request):
        try:
            access_token  = request.headers.get('Authorization')

            if not access_token:
                return JsonResponse({'message' : 'DOES_NOT_EXITS_ERROR'}, status=401)

            kakao_api  = KakaoAPI(access_token=access_token)
            kakao_user = kakao_api.get_kakao_user()

            user, created = User.objects.get_or_create(kakao_pk = kakao_user['id'])

            if created:
                user.email       = kakao_user['kakao_account']['email'],
                user.profile_url = kakao_user['kakao_account']['profile']['profile_image_url']
                user.nick_name   = kakao_user['kakao_account']['profile']['nickname']
                user.kakao_pk    = kakao_user['id']
                user.save()

            result = {
                'email'         : user.email,
                'profile_image' : user.profile_url,
                'nick_name'     : user.nick_name
            }

            token = jwt.encode({'id' : user.id}, SECRET_KEY, ALGORITHM)

            return JsonResponse({'token' : token, 'data' : result}, status = 201)

        except IntegrityError:
            return JsonResponse({'message' : 'INTEGRITY_ERROR'},status=401)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)