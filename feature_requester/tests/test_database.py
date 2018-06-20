from feature_requester.tests.BaseTest import BaseTest


class TestDatabaseModels(BaseTest):

    def test_save_client(self):
        """When client is saved with success it should receive an id"""
        a_client = self.create_client()
        a_client.save()
        self.assertEqual(a_client.id, 1)

    def test_save_feature(self):
        """When feature is saved with success it should receive an id"""
        a_feature = self.create_feature()
        a_feature.save()
        self.assertEqual(a_feature.id, 1)
