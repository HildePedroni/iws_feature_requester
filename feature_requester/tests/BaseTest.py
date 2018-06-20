from unittest import TestCase

from feature_requester import create_app, db
from feature_requester.config import TestConfig
from feature_requester.models import Client, Feature


class BaseTest(TestCase):

    @classmethod
    def setUpClass(cls):
        """On inherited classes, run our `setUp` method"""
        if cls is not BaseTest and cls.setUp is not BaseTest.setUp:
            orig_setup = cls.setUp

            def setUpOverride(self, *args, **kwargs):
                BaseTest.setUp(self)
                return orig_setup(self, *args, **kwargs)

            cls.setUp = setUpOverride

    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def create_client(self, client_name='Client A'):
        client = Client(name=client_name)
        return client

    def create_feature(self, client=None, client_name='Client A', priority=1):
        client = client if client else self.create_client(client_name)

        new_feature = Feature(
            title='New request feature',
            description='Wants a form do make feature requests',
            target_date='2018-07-10',
            priority=priority,
            product_area='Billing',
            client=client
        )
        return new_feature

    def create_test_features(self, how_many=1, client_name=None, client=None):
        """
        Will return clients with names in sequence
        Client 1, Client 2, ... ,Client n
        """

        for num in range(how_many):
            if client:
                a_feature = self.create_feature(client=client, priority=num + 1)
            else:
                a_feature = self.create_feature(
                    client_name=client_name
                    if client_name
                    else 'Client ' + str(num + 1),
                    priority=num + 1
                )
            a_feature.save()
