# coding=utf-8

import requests
from base import ApiServerUnittest


class TestApiServer(ApiServerUnittest):
    def setUp(self):
        super(TestApiServer, self).setUp()
        self.host = 'http://127.0.0.1:4555'
        self.api_client = requests.Session()
    
    def tearDown(self):
        super(TestApiServer, self).setUp()

    def test_create_user_not_existed(self):
        url = '%s/api/users/%d' % (self.host, 1000)
        json = {
          'name':'user1',
          'password':'123456'
        }
        resp = self.api_client.post(url,data=json)

        self.assertEqual(201, resp.status_code)
        self.assertEqual(True,resp.json()['success'])