from sqlalchemy import and_

from feature_requester import db
from feature_requester.models import Client, Feature


def get_client_or_create(client_name):
    client = Client.query.filter_by(name=client_name).first()
    # Check if client already exists, if not, create one
    if client is None:
        client = Client(name=client_name)
        client.save()

    return client


def swap_features_priority(client, feature, new_priority):
    feature_to_swap = Feature.query.filter(
        and_(Feature.client == client,
             Feature.priority == new_priority)).first()
    if feature_to_swap is not None:
        feature_to_swap.priority = feature.priority

    feature.priority = new_priority
    db.session.commit()


def reorder_features_for_client(client, feature):
    client_features = Feature.query.filter(
        and_(Feature.client == client,
             Feature.priority >= feature.priority)).order_by(Feature.priority)

    last_feature_priority = 0
    for c_feature in client_features:
        if last_feature_priority != 0 and last_feature_priority < c_feature.priority:
            break
        else:
            last_feature_priority = c_feature.priority + 1
            feature_to_update = Feature.query.get_or_404(c_feature.id)
            feature_to_update.priority += 1
            db.session.commit()
