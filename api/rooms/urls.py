from django.urls       import path, include
from .views.main       import SearchRoomView, RoomSuggestionView
from .views.detail     import RoomView
from .views.map        import RoomListView, RoomGroupView
from .views.drfview    import RoomAPIView, RoomDetailAPIView, RoomSearchAPIView, AddressSearchAPIView, PostViewSet
from rest_framework.routers  import DefaultRouter

router = DefaultRouter()
router.register('viewset', PostViewSet)
urlpatterns = [
    path('/',include(router.urls)),
]


# urlpatterns = [
#     # path('/<int:room_id>', RoomView.as_view()),
#     path('', RoomListView.as_view()),
#     # path('/search', SearchRoomView.as_view()),
#     path('/search', RoomSearchAPIView.as_view()),
#     path('/all', RoomAPIView.as_view()),
#     path('/suggestion', RoomSuggestionView.as_view()),
#     path('/maps', RoomGroupView.as_view()),
#     path('/list', PostViewSet.as_view()),
#     path('/<int:pk>', RoomDetailAPIView.as_view()),
#     path('/address', AddressSearchAPIView.as_view())
# ]

