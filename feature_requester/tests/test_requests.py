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

    def test_patch_invalid_id(self):
        """should return status 404"""
        url = 'api/feature/{}'.format(200)
        data = {
            'client': {
                'name': 'Client A'
            },
            'title': 'New request feature',
            'description': 'Wants a form do make feature requests',
            'target_date': '2018-07-10',
            'product_area': 'Billing',
            'priority': 1
        }
        response = self.request_client.patch(
            url,
            headers={'Accept': 'application/json',
                     'Content-Type': 'application/json'},
            data=json.dumps(data))

        self.assertEqual(response.status_code, 404)

    def test_patch_update(self):
        """Should update the priority"""
        # first we create a feature
        self.a_feture = self.create_feature(client_name='Client A', priority=3)
        self.a_feture.save()

        # changing the priority
        data = {
            'client': {
                'name': 'Client A'
            },
            'title': 'New request feature',
            'description': 'Wants a form do make feature requests',
            'target_date': '2018-07-10',
            'product_area': 'Billing',
            'priority': 1
        }
        url = 'api/feature/{}'.format(self.a_feture.id)
        response = self.request_client.patch(
            url,
            headers={'Accept': 'application/json',
                     'Content-Type': 'application/json'},
            data=json.dumps(data))

        result_data = json.loads(response.data.decode('utf-8'))

        expected_id_priority = (1, 1)
        result = (
            result_data['feature']['id'], result_data['feature']['priority'])

        self.assertEqual(result, expected_id_priority)

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
