from api.users.views import KakaoSigninView
from django.urls import path

from .views import KakaoSigninView

urlpatterns = [
    path('/signin', KakaoSigninView.as_view())
]