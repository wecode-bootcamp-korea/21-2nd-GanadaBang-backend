from django.urls import path

from .views.detail import RoomView

urlpatterns = [
    path('/<int:room_id>',RoomView.as_view())
]