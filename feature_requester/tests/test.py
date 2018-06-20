from unittest import TestCase

from feature_requester import create_app
# first test file. It will be refactored with the tests growth
from feature_requester.config import TestConfig


class Test(TestCase):

    def setUp(self):
        self.app = create_app(TestConfig)
        self.request_client = self.app.test_client(self)

    def test_home_url(self):
        """get on / should return status 200"""
        resp = self.request_client.get('/')
        self.assertEqual(200, resp.status_code)

    def test_create_new_feature_url(self):
        """post on /api/feature should return status 200"""
        resp = self.request_client.post('/api/feature')
        self.assertEqual(200, resp.status_code)

    def test_patch_feature_url(self):
        """patch on /api/feature/id should return status 200"""
        resp = self.request_client.patch('/api/feature/1')
        self.assertEqual(200, resp.status_code)

    def test_delete_feature_url(self):
        """delete on /api/feature/id should return status 200"""
        resp = self.request_client.delete('/api/feature/1')
        self.assertEqual(200, resp.status_code)
