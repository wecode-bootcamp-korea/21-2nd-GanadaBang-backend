from django.urls   import path
from .views.main   import SearchRoomView, RoomSuggestionView
from .views.detail import RoomView
from .views.map    import RoomListView, RoomGroupView

urlpatterns = [
    path('', RoomListView.as_view()),
    path('/<int:room_id>', RoomView.as_view()),
    path('/search', SearchRoomView.as_view()),
    path('/suggestion', RoomSuggestionView.as_view()),
    path('/maps', RoomGroupView.as_view()),
]