import unittest,jwt
from django.http import response

from django.test   import TestCase, Client
from unittest.mock import MagicMock, patch

from my_settings      import SECRET_KEY, ALGORITHM
from api.users.models import User

class KakaoSigninViewTest(TestCase):
    @patch('api.users.views.requests')
    def test_kakaosignin_success(self, mocked_requests):
        client = Client()

        class MockedResponse:
            def json(self):
                return {
                    "id": 21,
                    "kakao_account": {
                        "profile": {
                            "nickname": "성규짱짱맨",
                            "profile_image_url": "http://k.kakaocdn.net/image_url",
                        },
                        "email": "zzangmankim@kakao.com"
                    }
                }
        mocked_requests.get = MagicMock(return_value = MockedResponse())
        headers             = {'HTTP_Authorization' : 'fake_token'}
        response            = client.post('/api/users/signin', content_type='applications/json', **headers)
        user                = User.objects.get(email = 'zzangmankim@kakao.com')

        result = {
            'email'         : user.email,
            'profile_image' : user.profile_url,
            'nick_name'     : user.nick_name
        }

        token = jwt.encode({'id': user.id},SECRET_KEY, ALGORITHM)

        self.assertEqual(response.json(), {'token' : token, 'data' : result})
        self.assertEqual(response.status_code, 201)

    @patch('api.users.views.requests')
    def test_kakaosignin_access_token_does_not_exit_error(self, mocked_requests):
        client = Client()

        class MockedResponse:
            def json(self):
                return {
                    "id": 21,
                    "kakao_account": {
                        "profile": {
                            "nickname": "성규짱짱맨",
                            "profile_image_url": "http://k.kakaocdn.net/image_url",
                        },
                        "email": "zzangmankim@kakao.com"
                    }
                }
        mocked_requests.get = MagicMock(return_value = MockedResponse())
        headers             = {'HTTP_Authorization' : ''}
        response            = client.post('/api/users/signin', content_type='applications/json', **headers)

        self.assertEqual(response.json(), {'message' : 'DOES_NOT_EXITS_ERROR'})
        self.assertEqual(response.status_code, 401)

    @patch('api.users.views.requests')
    def test_kakaosignin_invalid_token_error(self, mocked_requests):
        client = Client()

        class MockedResponse:
            def json(self):
                return {}

        mocked_requests.get = MagicMock(return_value = MockedResponse())
        headers             = {'HTTP_Authorization' : 'fake_token'}
        response            = client.post('/api/users/signin', content_type='applications/json', **headers)

        self.assertEqual(response.json(), {'message' : 'INVALID_TOKEN'})
        self.assertEqual(response.status_code, 401)

    @patch('api.users.views.requests')
    def test_kakaosignin_integrity_error(self, mocked_requests):
        client = Client()

        class MockedResponse:
            def json(self):
                return {
                    "kakao_account": {
                        "profile": {
                            "nickname": "성규짱짱맨",
                            "profile_image_url": "http://k.kakaocdn.net/image_url",
                        },
                        "email": "zzangmankim@kakao.com"
                    }
                }
        mocked_requests.get = MagicMock(return_value = MockedResponse())
        headers             = {'HTTP_Authorization' : 'fake_token'}
        response            = client.post('/api/users/signin', content_type='applications/json', **headers)

        self.assertEqual(response.json(), {'message' : 'INTEGRITY_ERROR'})
        self.assertEqual(response.status_code, 401)

    @patch('api.users.views.requests')
    def test_kakaosignin_key_error(self, mocked_requests):
        client = Client()

        class MockedResponse:
            def json(self):
                return {
                    "id": 21,
                    "kakao_account_error": {
                        "profile": {
                            "nickname": "성규짱짱맨",
                            "profile_image_url": "http://k.kakaocdn.net/image_url",
                        },
                        "email": "zzangmankim@kakao.com"
                    }
                }
        mocked_requests.get = MagicMock(return_value = MockedResponse())
        headers             = {'HTTP_Authorization' : 'fake_token'}
        response            = client.post('/api/users/signin', content_type='applications/json', **headers)

        self.assertEqual(response.json(), {'message' : 'KEY_ERROR'})
        self.assertEqual(response.status_code, 400)