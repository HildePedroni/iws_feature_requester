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
        """Should return 404 not found"""
        self.resp = self.request_client.get('/api/feature/1245')
        self.assertEqual(404, self.resp.status_code)


class TestFeature(BaseTest):

    def setUp(self):
        super(BaseTest, self).setUpClass()
        self.request_client = self.app.test_client(self)
        self.url = '/api/feature'

    def test_new_feature_post_invalid(self):
        """should return 400 bad request"""
        data = {}
        response = self.post_data(self.url, data)
        self.assertEqual(400, response.status_code)

    def test_new_feature(self):
        """Should return the new created feature as a json"""
        {"title": "qweqweqweqwe",
         "description": "qweqweqweqweeqw",
         "client": "Client B",
         "target_date": "2018-06-30",
         "priority": "4",
         "product_area": "Billing"}


        data = {
            'client': {
                'name': 'Client A'
            },
            'title': 'Hello',
            'description': 'Here comes some description',
            'target_date': '2018-06-16',
            'product_area': 'Billing',
            'priority': 1
        }
        response = self.post_data(self.url, data)
        data = json.loads(response.data.decode('utf-8'))
        result_id = data['feature']['id']
        expected_id = 1
        self.assertEqual(result_id, expected_id)

    def test_feature_reordering(self):
        pass

    def post_data(self, url, data):
        """Auxiliar method to send post requests with
            it receives the url, and a dictionay
        """
        response = self.request_client.post(
            url,
            headers={
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            data=json.dumps(data)
        )
        return response
