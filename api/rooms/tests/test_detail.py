from django.test            import TestCase,Client

from api.rooms.models import Location, Option, RoomType, TradeType, Room, OptionType, RoomImage, RoomOption

class RoomViewTest(TestCase):
    def setUp(self):

        Location.objects.create(
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
        )

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

        a = Room.objects.create(id='1',title='원룸1',content='매물정보 원룸 1 풀옵션 ',
                        location_id='1',room_type_id='1',trade_type_id='1',monthly_rent='30',
                        deposit='100',sale='0',agent='성규부동산',floor='1',room_area='10.12',
                        room_count='1',bathroom_count='1',heating_type='개별',elevator='유')
        a.created_at = '2021-06-28T19:50:19.403'
        a.save()

        OptionType.objects.bulk_create([
            OptionType(id='1',name='NORMAL'),
            OptionType(id='2',name='SECURITY')
        ])

        RoomImage.objects.create(id='1',room_id='1',url='https://i.imgur.com/SwiHvRG.png')

        Option.objects.bulk_create([
            Option(id='1',name='에어컨',
            image_url='https://www.dabangapp.com/static/media/aircondition.e635232d.svg',
            option_type_id='1'),
            Option(id='13',name='전자도어락',
            image_url='https://www.dabangapp.com/static/media/doorlock.1b4ae1e7.svg',
            option_type_id='2')
            ])

        RoomOption.objects.bulk_create([
            RoomOption(id='1', room_id='1', option_id='1'),
            RoomOption(id='2', room_id='1', option_id='13')
        ])

    def test_roomview_get_succeess(self):
        client = Client()
        response = client.get('/api/rooms/1')
        self.assertEqual.__self__.maxDiff = None
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
                "message":{
                    "id"      : 1,
                    "title"   : "원룸1",
                    "content" : "매물정보 원룸 1 풀옵션 ",
                    "location": {
                        "id"       : 1,
                        "state"    : "서울특별시",
                        "city"     : "강남구",
                        "dong"     : "삼성동",
                        "detail"   : "테헤란로 427",
                        "latitude" : "37.50637292000000",
                        "longitude": "127.05364070000000"
                    },
                    "room_type"     : "ONE_ROOM",
                    "trade_type"    : "MONTHLY_RENT",
                    "monthly_rent"  : 30,
                    "deposit"       : 100,
                    "sale"          : 0,
                    "agent"         : "성규부동산",
                    "floor"         : 1,
                    "room_area"     : 10.12,
                    "room_count"    : 1,
                    "bathroom_count": 1,
                    "heating_type"  : "개별",
                    "elevator"      : "유",
                    "created_at"    : "2021-06-28T19:50:19.403",
                    "image"         : [
                        "https://i.imgur.com/SwiHvRG.png"
                    ],
                    "normal_option":[
                        {
                            "name"       : "에어컨",
                            "image_url"  : "https://www.dabangapp.com/static/media/aircondition.e635232d.svg",
                            "option_type": "NORMAL"
                        }
                    ],
                    "security_option":[
                        {
                            "name"       : "전자도어락",
                            "image_url"  : "https://www.dabangapp.com/static/media/doorlock.1b4ae1e7.svg",
                            "option_type": "SECURITY"
                        }
                    ]
                }
            })
    def test_roomview_get_failed(self):
        client = Client()
        response = client.get('/api/rooms/2')
        self.assertEqual(response.status_code, 404)