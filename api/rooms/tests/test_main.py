from unittest.mock import patch, MagicMock

from django.test import TestCase, Client

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
                                                                'point': {'x': '127.094374999', 'y': '37.5133333304'
                                                                        }
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
    def test_invalide_error_get(self, mocked_requests):
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
                                'geometry': 'http://map.vworld.kr/data/geojson/district/11710101.geojson',
                                'point': {'x': '127.094374999', 'y': '37.5133333304'}
                            }]
                        }
                    }
                }
        mocked_requests.get = MagicMock(return_value = MockedResponse())
        response            = client.get("/api/rooms/search", {'address' : '잠실동', 'type': 'distirct','category' : 'L4'})
        self.assertEqual(response.status_code, 400)