from unittest.mock    import MagicMock, patch

from django.test      import TestCase, Client

from api.rooms.models import Location, RoomType, TradeType, Room, OptionType, RoomImage

class MapRoomTestCase(TestCase):
    def setUp(self):
        Location.objects.bulk_create([
            Location(
                id        = '1',
                state     = '서울특별시',
                city      = '강남구',
                dong      = '삼성동',
                detail    = '테헤란로 427',
                latitude  = '37.50637292',
                longitude = '127.0536407',
                utmk_x    = '1945020.83739406',
                utmk_y    = '960738.939126282',
                dong_code = '11680105'
            ),
            Location(
                id        = '10',
                state     = '서울특별시',
                city      = '서초구',
                dong      = '서초동',
                detail    = '서초대로70길 51',
                latitude  = '37.49206332',
                longitude = '127.0249488',
                utmk_x    = '1943445.64310341',
                utmk_y    = '958195.044413563',
                dong_code = '11650108')
        ])

        RoomType.objects.bulk_create([
            RoomType(id='1',name='ONE_ROOM'),
            RoomType(id='2',name='MULTI_ROOM'),
            RoomType(id='3',name='OFFICETEL')
        ])

        TradeType.objects.bulk_create([
            TradeType(id='1',name='MONTHLY_RENT'),
            TradeType(id='2',name='DEPOSIT'),
            TradeType(id='3',name='SALE')
        ])

        Room.objects.bulk_create([
            Room(id='1',title='원룸1',content='매물정보 원룸 1 풀옵션 ',
                        location_id='1',room_type_id='1',trade_type_id='1',monthly_rent='30',
                        deposit='100',sale='0',agent='성규부동산',floor='1',room_area='10.12',
                        room_count='1',bathroom_count='1',heating_type='개별',elevator='유'),
            Room(id='10',title='투룸5',content='매물정보 투룸 5 풀옵션',
                        location_id='10',room_type_id='2',trade_type_id='2',monthly_rent='0',
                        deposit='18000',sale='0',agent='민기부동산',floor='10',room_area='48.14',
                        room_count='2',bathroom_count='1',heating_type='지역',elevator='무')
        ])

        OptionType.objects.bulk_create([
            OptionType(id='1',name='NORMAL'),
            OptionType(id='2',name='SECURITY')
        ])
        
        RoomImage.objects.bulk_create([
            RoomImage(id='1',room_id='1',url='https://i.imgur.com/SwiHvRG.png'),
            RoomImage(id='10',room_id='10',url='https://i.imgur.com/lgc9RHI.png')
        ])

    def test_if_querry_string_is_empty(self):
        client   = Client()
        response = client.get('/api/rooms')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['room_list'],
            [{
                'city'         : '강남구',
                'content'      : '매물정보 원룸 1 풀옵션 ',
                'desposit'     : 100,
                'dong'         : '삼성동',
                'floor'        : 1,
                'id'           : 1,
                'location'     : {'y': 37.50637292, 'x': 127.0536407},
                'monthly_rent' : 30,
                'room_area'    : 10.12,
                'room_count'   : 1,
                'room_image'   : 'https://i.imgur.com/SwiHvRG.png',
                'room_type'    : 'ONE_ROOM',
                'sale'         : 0,
                'state'        : '서울특별시',
                'title'        : '원룸1',
                'trade_type'   : 'MONTHLY_RENT'
            },
            {
                'id'          : 10,
                'title'       : '투룸5',
                'content'     : '매물정보 투룸 5 풀옵션',
                'floor'       : 10,
                'room_count'  : 2,
                'room_area'   : 48.14,
                'desposit'    : 18000,
                'monthly_rent': 0,
                'sale'        : 0,
                'room_type'   : 'MULTI_ROOM',
                'trade_type'  : 'DEPOSIT',
                'room_image'  : 'https://i.imgur.com/lgc9RHI.png',
                'state'       : '서울특별시',
                'city'        : '서초구',
                'dong'        : '서초동',
                'location'    : {'y': 37.49206332, 'x': 127.0249488}}
            ])
    
    def test_not_located_any_room(self):
        client   = Client()
        response = client.get('/api/rooms', 
                    {'location' : '[[1,2],[1,2]]'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['room_list'], [])
        
    def test_located_room(self):
        client   = Client()
        response = client.get('/api/rooms', 
                    {'location' : '[[127.0536400,37.50637290], [127.0536408,37.50637293]]'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['room_list'],
            [{
                'city'         : '강남구',
                'content'      : '매물정보 원룸 1 풀옵션 ',
                'desposit'     : 100,
                'dong'         : '삼성동',
                'floor'        : 1,
                'id'           : 1,
                'location'     : {'y': 37.50637292, 'x': 127.0536407},
                'monthly_rent' : 30,
                'room_area'    : 10.12,
                'room_count'   : 1,
                'room_image'   : 'https://i.imgur.com/SwiHvRG.png',
                'room_type'    : 'ONE_ROOM',
                'sale'         : 0,
                'state'        : '서울특별시',
                'title'        : '원룸1',
                'trade_type'   : 'MONTHLY_RENT'
            }
        ])

    def test_filter_room_type(self):
        client   = Client()
        response = client.get('/api/rooms', {'filter' : '{"roomType" : [1]}'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['room_list'],
            [{
                'city'         : '강남구',
                'content'      : '매물정보 원룸 1 풀옵션 ',
                'desposit'     : 100,
                'dong'         : '삼성동',
                'floor'        : 1,
                'id'           : 1,
                'location'     : {'y': 37.50637292, 'x': 127.0536407},
                'monthly_rent' : 30,
                'room_area'    : 10.12,
                'room_count'   : 1,
                'room_image'   : 'https://i.imgur.com/SwiHvRG.png',
                'room_type'    : 'ONE_ROOM',
                'sale'         : 0,
                'state'        : '서울특별시',
                'title'        : '원룸1',
                'trade_type'   : 'MONTHLY_RENT'
            }
        ])

    def test_filter_trade_type(self):
        client = Client()
        response = client.get('/api/rooms', {'filter' : '{"tradeType" : [2]}'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['room_list'],
            [{
                'id'           : 10,
                'title'        : '투룸5',
                'content'      : '매물정보 투룸 5 풀옵션',
                'floor'        : 10,
                'room_count'   : 2,
                'room_area'    : 48.14,
                'desposit'     : 18000,
                'monthly_rent' : 0,
                'sale'         : 0,
                'room_type'    : 'MULTI_ROOM',
                'trade_type'   : 'DEPOSIT',
                'room_image'   : 'https://i.imgur.com/lgc9RHI.png',
                'state'        : '서울특별시',
                'city'         : '서초구',
                'dong'         : '서초동',
                'location'     : {'y': 37.49206332, 'x': 127.0249488}}
            ])

    def test_filter_room_and_trade_type(self):
        client   = Client()
        response = client.get('/api/rooms', 
                    {'filter' : '{"tradeType" : [2], "roomType" : [2]}'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['room_list'],
            [{
                'id'           : 10,
                'title'        : '투룸5',
                'content'      : '매물정보 투룸 5 풀옵션',
                'floor'        : 10,
                'room_count'   : 2,
                'room_area'    : 48.14,
                'desposit'     : 18000,
                'monthly_rent' : 0,
                'sale'         : 0,
                'room_type'    : 'MULTI_ROOM',
                'trade_type'   : 'DEPOSIT',
                'room_image'   : 'https://i.imgur.com/lgc9RHI.png',
                'state'        : '서울특별시',
                'city'         : '서초구',
                'dong'         : '서초동',
                'location'     : {'y': 37.49206332, 'x': 127.0249488}}
            ])


class MapGroupRoomTestCase(TestCase):
    def setUp(self):
        Location.objects.bulk_create([
            Location(
                id        = '1',
                state     = '서울특별시',
                city      = '강남구',
                dong      = '삼성동',
                detail    = '테헤란로 427',
                latitude  = '37.50637292',
                longitude = '127.0536407',
                utmk_x    = '1945020.83739406',
                utmk_y    = '960738.939126282',
                dong_code = '11680105'
            ),
            Location(
                id        = '10',
                state     = '서울특별시',
                city      = '서초구',
                dong      = '서초동',
                detail    = '서초대로70길 51',
                latitude  = '37.49206332',
                longitude = '127.0249488',
                utmk_x    = '1943445.64310341',
                utmk_y    = '958195.044413563',
                dong_code = '11650108')
        ])

        RoomType.objects.bulk_create([
            RoomType(id='1',name='ONE_ROOM'),
            RoomType(id='2',name='MULTI_ROOM'),
            RoomType(id='3',name='OFFICETEL')
        ])

        TradeType.objects.bulk_create([
            TradeType(id='1',name='MONTHLY_RENT'),
            TradeType(id='2',name='DEPOSIT'),
            TradeType(id='3',name='SALE')
        ])

        Room.objects.bulk_create([
            Room(id='1',title='원룸1',content='매물정보 원룸 1 풀옵션 ',
                        location_id='1',room_type_id='1',trade_type_id='1',monthly_rent='30',
                        deposit='100',sale='0',agent='성규부동산',floor='1',room_area='10.12',
                        room_count='1',bathroom_count='1',heating_type='개별',elevator='유'),
            Room(id='10',title='투룸5',content='매물정보 투룸 5 풀옵션',
                        location_id='10',room_type_id='2',trade_type_id='2',monthly_rent='0',
                        deposit='18000',sale='0',agent='민기부동산',floor='10',room_area='48.14',
                        room_count='2',bathroom_count='1',heating_type='지역',elevator='무')
        ])

        OptionType.objects.bulk_create([
            OptionType(id='1',name='NORMAL'),
            OptionType(id='2',name='SECURITY')
        ])
        
        RoomImage.objects.bulk_create([
            RoomImage(id='1',room_id='1',url='https://i.imgur.com/SwiHvRG.png'),
            RoomImage(id='10',room_id='10',url='https://i.imgur.com/lgc9RHI.png')
        ])


    @patch('api.rooms.views.map.requests')
    def test_group_by_state(self, mocked_requests):
        client = Client()

        class MockRequestResponse:
            def __init__(self, json_body):
                self.json_body = json_body
            
            def json(self):
                return self.json_body

        mocked_requests.get.side_effect = [
            MockRequestResponse({
                "response": {
                    "result": {
                        "items": [
                            {
                                "id": "11",
                                "title": "서울특별시",
                                "point": {
                                    "x": "126.97837448",
                                    "y": "37.56667076"
                                }
                            }
                        ]
                    }
                }
            })]

        response = client.get('/api/rooms/maps', {'zoom':8})
        
        self.assertEqual(response.json(), {
            'markers': [
            {
                'name'  : '서울특별시',
                'count' : 2,
                'code'  : '11',
                'lng'   : '126.97837448',
                'lat'   : '37.56667076'
            }]})


    @patch('api.rooms.views.map.requests')
    def test_group_by_city(self, mocked_requests):
        client = Client()

        class MockRequestResponse:
            def __init__(self, json_body):
                self.json_body = json_body
            
            def json(self):
                return self.json_body

        mocked_requests.get.side_effect =[
            MockRequestResponse({
                "response": {
                    "result": {
                        "items": [
                            {
                                "id": "11680",
                                "title": "서울특별시 강남구",
                                "point": {
                                    "x": "127.04739059",
                                    "y": "37.51735491"
                                }
                            }
                        ]
                    }
                }
            }),
            MockRequestResponse({
                "response": {
                    "result": {
                        "items": [
                            {
                                "id": "11650",
                                "title": "서울특별시 서초구",
                                "point": {
                                    "x": "127.03269066",
                                    "y": "37.48363159"
                                }
                            }
                        ]
                    }
                }
            })
        ]

        response = client.get('/api/rooms/maps', {'zoom':10})
        
        self.assertEqual(response.json(), {
            'markers': [{
                'name': '강남구',
                'count': 1,
                'code': '11680',
                'lng': '127.04739059',
                'lat': '37.51735491'
            }, 
            {
                'name': '서초구', 
                'count': 1, 'code': '11650', 
                'lng': '127.03269066', 
                'lat': '37.48363159'
            }]})

    @patch('api.rooms.views.map.requests')
    def test_group_by_dong(self, mocked_requests):
        client = Client()

        class MockRequestResponse:
            def __init__(self, json_body):
                self.json_body = json_body
            
            def json(self):
                return self.json_body

        mocked_requests.get.side_effect = [
            MockRequestResponse({
                "response": {
                    "result": {
                        "items": [
                            {
                                "id": "11680105",
                                "title": "서울특별시 강남구 삼성동",
                                "point": {
                                    "x": "127.045953",
                                    "y": "37.511156"
                                }
                            }
                        ]
                    }
                }
            }),
            MockRequestResponse({
                "response": {
                    "result": {
                        "items": [
                            {
                                "id": "11650108",
                                "title": "서울특별시 서초구 서초동",
                                "point": {
                                    "x": "127.0125",
                                    "y": "37.4836096001"
                                }
                            }
                        ]
                    }
                }
            })
        ]

        response = client.get('/api/rooms/maps', {'zoom':13})
        
        self.assertEqual(response.json(), {
            'markers': [{
                'name'  : '삼성동',
                'count' : 1,
                'code'  : '11680105',
                'lng'   : '127.045953',
                'lat'   : '37.511156'
            }, 
            {
                'name'  : '서초동',
                'count' : 1,
                'code'  : '11650108',
                'lng'   : '127.0125',
                'lat'   : '37.4836096001'
            }]})