import json

from feature_requester.tests.BaseTest import BaseTest


class TestGetRequests(BaseTest):

    def setUp(self):
        super(BaseTest, self).setUpClass()
        self.request_client = self.app.test_client(self)

        self.create_test_features(how_many=4)
        self.resp = self.request_client.get('/api/feature')

    def test_get_feature_url(self):
        """get on /api/feature should return status 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_get_features(self):
        """The method shoul return a json with clients with names in sequence"""
        data = json.loads(self.resp.data.decode('utf-8'))

        features = data['features']

        expected = ('Client 1', 'Client 2', 'Client 3', 'Client 4')

        for index, feature in enumerate(features):
            with self.subTest():
                self.assertEqual(feature['client']['name'], expected[index])


class TestGetByIdRequests(BaseTest):
    def setUp(self):
        super(BaseTest, self).setUpClass()
        self.request_client = self.app.test_client(self)

        self.create_test_features(how_many=1)
        self.resp = self.request_client.get('/api/feature/1')

    def test_get_feature_by_id_url(self):
        """get on /api/feature/id should return status 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_get_feature(self):
        """Should return the first feature with Client 1"""
        data = json.loads(self.resp.data.decode('utf-8'))
        expected = 'Client 1'
        result = data['feature']['client']['name']

        self.assertEqual(result, expected)

    def test_get_feature_with_invalid_id(self):
        """Should return 404"""
        self.resp = self.request_client.get('/api/feature/1245')
        self.assertEqual(404, self.resp.status_code)
