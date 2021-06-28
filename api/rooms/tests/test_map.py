from django.test import TestCase, Client

from api.rooms.models import Location, RoomType, TradeType, Room, OptionType, RoomImage

class MapRoomTestCase(TestCase):
    def setUp(self):
        Location.objects.bulk_create([
            Location(id='1',state='서울특별시',city='강남구',dong='삼성동',
                    detail='테헤란로 427',latitude='37.50637292',longitude='127.0536407',
                    utmk_x='1945020.83739406',utmk_y='960738.939126282'),
            Location(id='10',state='서울특별시',city='서초구',dong='서초동',
                    detail='서초대로70길 51',latitude='37.49206332',longitude='127.0249488',
                    utmk_x='1943445.64310341',utmk_y='958195.044413563')
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