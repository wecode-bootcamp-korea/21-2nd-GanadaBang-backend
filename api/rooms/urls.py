from django.urls   import path

from .views.detail import RoomView
from .views.map    import RoomListView

urlpatterns = [
    path('/<int:room_id>',RoomView.as_view()),
    path('', RoomListView.as_view()),
]
