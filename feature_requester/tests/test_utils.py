from feature_requester.api import utils
from feature_requester.models import Feature
from feature_requester.tests.BaseTest import BaseTest


class TestUtils(BaseTest):

    def setUp(self):
        super(BaseTest, self).setUpClass()
        self.client = self.create_client(client_name='Client A')
        self.client.save()

    def test_get_client_or_create_non_exists(self):
        """Should return a new Client"""
        a_client = utils.get_client_or_create('Client B')
        self.assertEqual(a_client.id, 2)

    def test_get_client_or_create_exists(self):
        """Should return a already created client"""
        a_client = utils.get_client_or_create('Client A')
        self.assertEqual(a_client.id, 1)

    def test_reorder_features_for_client(self):
        """Order of features ids should be 1,2,5, and 4"""
        self.create_test_features(how_many=4, client=self.client)
        a_feature = self.create_feature(client=self.client, priority=3)

        utils.reorder_features_for_client(client=self.client, feature=a_feature)
        a_feature.save()
        client_features = Feature.query.filter(
            Feature.client == self.client).order_by(Feature.priority)

        expected_id_priority = ((1, 1), (2, 2), (5, 3), (3, 4), (4, 5),)

        for i, feature in enumerate(client_features):
            with self.subTest():
                dic1 = {'id': expected_id_priority[i][0],
                        'priority': expected_id_priority[i][1]}
                dic2 = {'id': feature.id,
                        'priority': feature.priority}
                self.assertEqual(dic1, dic2)

    def test_reorder_update_for_client(self):
        """Order of features ids should be 1,3,2, and 4"""
        self.create_test_features(how_many=4, client=self.client)
        a_feature = Feature.query.get_or_404(3)

        utils.swap_features_priority(client=self.client,
                                     feature=a_feature,
                                     new_priority=2)

        client_features = Feature.query.filter(
            Feature.client == self.client).order_by(Feature.priority)

        expected_id_priority = ((1, 1), (3, 2), (2, 3), (4, 4),)

        for i, feature in enumerate(client_features):
            with self.subTest():
                dic1 = {'id': expected_id_priority[i][0],
                        'priority': expected_id_priority[i][1]}
            dic2 = {'id': feature.id,
                    'priority': feature.priority}
            self.assertEqual(dic1, dic2)
