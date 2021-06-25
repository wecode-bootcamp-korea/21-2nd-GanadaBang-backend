from unittest.mock import patch, MagicMock

from django.test import TestCase, Client

from api.rooms.models import  Location, RoomType, TradeType, Room, RoomImage

class AddressSearchTest(TestCase):
    @patch('api.rooms.views.main.requests')
    def test_get(self, mocked_requests):
        client = Client()
        
        class MockedResponse:
            def json(self):
                return {
                    'response': {
                        'service': {
                            'name': 'search',
                             'version': '2.0', 
                             'operation': 'search', 
                             'time': '7(ms)'
                        }, 
                        'status': 'OK', 
                        'record': {
                            'total': '1',
                            'current': '1'
                        }, 
                        'page': {
                            'total': '1', 
                            'current': '1', 
                            'size': '100'
                        },
                        'result': {
                            'crs': 'EPSG:4326',
                            'type': 'district',
                            'items': [{
                                'id': '11710101',
                                'title': '서울특별시 송파구 잠실동',
                                'geometry': 'http://map.vworld.kr/data/geojson/district/11710101.geojson',
                                'point': {'x': '127.094374999', 'y': '37.5133333304'}
                            }]
                        }
                    }
                }
                   
        mocked_requests.get = MagicMock(return_value = MockedResponse())
        response = client.get("/api/rooms/search", {'address' : '잠실동', 'type' : 'district', 'category' : 'L4'})
        self.assertEqual(response.status_code, 200)
        
class AddressSearchTest(TestCase):
    @patch('api.rooms.views.main.requests')
    def test_status_error_get(self, mocked_requests):
        client = Client()
    
        class MockedResponse:
             def json(self):
                return {
                    'response': {
                        'service': {
                            'name': 'search',
                             'version': '2.0', 
                             'operation': 'search', 
                             'time': '7(ms)'
                        }, 
                        'status': 'OK', 
                        'record': {
                            'total': '1',
                            'current': '1'
                        }, 
                        'page': {
                            'total': '1', 
                            'current': '1', 
                            'size': '100'
                        },
                        'result': {
                            'crs': 'EPSG:4326',
                            'type': 'district',
                            'items': [{
                                'id': '11710101',
                                'title': '서울특별시 송파구 잠실동',
                                'geometry': 'http://map.vworld.kr/data/geojson/district/11710101.geojson',
                                'point': {'x': '127.094374999', 'y': '37.5133333304'}
                            }]
                        }
                    }
                }
        mocked_requests.get = MagicMock(return_value = MockedResponse())
        response            = client.get("/api/rooms/search", {'address' : '잠실동', 'category' : 'L4'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message':'VALUE_ERROR'})
        
class AddressSearchTest(TestCase):
    @patch('api.rooms.views.main.requests')
    def test_error_type_get(self, mocked_requests):
        client = Client()
        
        class MockedResponse:
            def json(self):
                    return {
                        'response': {
                    'service': {
                        'name': 'search',
                            'version': '2.0', 
                            'operation': 'search', 
                            'time': '7(ms)'
                    }, 
                    'status': 'ERROR', 
                    'record': {
                        'total': '1',
                        'current': '1'
                    }, 
                    'page': {
                        'total': '1', 
                        'current': '1', 
                        'size': '100'
                    },
                    'result': {
                        'crs': 'EPSG:4326',
                        'type': 'district',
                        'items': [{
                            'id': '11710101',
                            'title': '서울특별시 송파구 잠실동',
                            'geometry': 'http://map.vworld.kr/data/geojson/district/11710101.geojson',
                            'point': {'x': '127.094374999', 'y': '37.5133333304'}
                        }]
                    }
                }
           }
        mocked_requests.get = MagicMock(return_value = MockedResponse())
        response            = client.get("/api/rooms/search", {'address' : '잠실동', 'type':'district', 'category' : 'L4'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message':'VALUE_ERROR'})
        
class MainUnitTest(TestCase):
    def setUp(self):
        Location.objects.create(
            id        = '1',
            state     = '서울특별시',
            city      = '강남구',
            dong      = '삼평동',
            detail    = '테헤란로 427',
            latitude  = '37.50637292',
            longitude = '127.0536407',
            utmk_x    = '1945020.83739406',
            utmk_y    = '960738.939126282',
            dong_code = '12344'
            )
        
        RoomType.objects.create(
            id   = '1',
            name = 'ONE_ROOM'
            )
          
        TradeType.objects.create(
            id   = '1',
            name = 'MONTHLY_RENT'
            )
            
        Room.objects.create(
            id             = '1',
            title          = '원룸1',
            content        = '매물정보 원룸 1 풀옵션',
            location_id    = '1',
            room_type_id   = '1',
            trade_type_id  = '1',
            monthly_rent   = '30',
            deposit        = '100',
            sale           = '0',
            agent          = '성규부동산',
            floor          = '1',
            room_area      = '10.12',
            room_count     = '1',
            bathroom_count = '1',
            heating_type   = '개별',
            elevator       = '유'
            )

        RoomImage.objects.create(
            id      = '1',
            room_id = '1',
            url     = 'https://i.imgur.com/SwiHvRG.png'
            )
        
    def tearDown(self):
        Location.objects.all().delete()
        RoomType.objects.all().delete()
        TradeType.objects.all().delete()
        Room.objects.all().delete()
        RoomImage.objects.all().delete()
           
    def test_main_suggestion(self): 
        client   = Client()
        response = client.get('/api/rooms/suggestion',{'keyword_sort':'삼평동', 'offset':'0', 'limit':'4'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
                "result":[{
                    "id"          : 1,
                    "title"       : "원룸1",
                    "content"     : "매물정보 원룸 1 풀옵션",
                    "floor"       : 1,
                    "room_count"  : 1,
                    "room_area"   : 10.12,
                    "deposit"     : 100,
                    "monthly_rent": 30,
                    "sale"        : 0,
                    "room_type"   : "ONE_ROOM",
                    "trade_type"  : "MONTHLY_RENT",
                    "room_image"  : "https://i.imgur.com/SwiHvRG.png",
                    "state"       : "서울특별시",
                    "city"        : "강남구",
                    'dong'        : "삼평동",
                    "dong_code"   : "12344"
                }]
            })        