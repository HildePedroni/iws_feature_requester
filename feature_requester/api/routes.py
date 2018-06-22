from flask import Blueprint, jsonify, request

from feature_requester import db
from feature_requester.api import utils
from feature_requester.models import Feature, FeatureSchema

api = Blueprint('api', __name__)

@api.route('/feature', methods=['GET'])
def get_all_features():
    """Returns a json array of all fetures in the database"""
    features = Feature.query.order_by(Feature.priority)
    feature_schema = FeatureSchema(many=True)
    output = feature_schema.dump(features).data
    return jsonify({'features': output}), 200


@api.route('/feature/<feature_id>', methods=['GET'])
def get_one_feature(feature_id):
    """Return a specific feature by id
       param required feature_id
    """
    feature_schema = FeatureSchema()
    feature = Feature.query.get_or_404(feature_id)
    output = feature_schema.dump(feature)

    return jsonify({'feature': output.data}), 200


@api.route('/feature', methods=['POST'])
def create_new_feature():
    """Create a new feature for the given Client
        params:
        title - string
        description - text
        client name - string
        product_area - string
        priority - integer
    """

    feature_schema = FeatureSchema()
    data = request.get_json()
    errors = feature_schema.validate(data)
    if errors:
        return jsonify({'errors': errors}), 400

    client_name = data['client']['name']
    client = utils.get_client_or_create(
        client_name=client_name
    )

    feature = Feature(
        title=data['title'],
        description=data['description'],
        target_date=data['target_date'],
        product_area=data['product_area'],
        priority=data['priority'],
        client=client
    )
    utils.reorder_features_for_client(client=client, feature=feature)
    feature.save()

    return jsonify({'feature': feature_schema.dump(feature).data}), 201


@api.route('/feature/<feature_id>', methods=['PATCH'])
def update_feature(feature_id):
    """Update a given feature by id
       param required id
    """
    data = request.get_json()
    feature_schema = FeatureSchema()
    errors = feature_schema.validate(data)
    if errors:
        return jsonify({'errors': errors}), 400

    client_name = data['client']['name']
    client = utils.get_client_or_create(
        client_name=client_name
    )
    feature = Feature.query.get_or_404(feature_id)
    if not feature:
        return jsonify({'errors': 'Feature not found'}), 404

    if feature.priority != data.get('priority'):
        utils.swap_features_priority(client=client,
                                     feature=feature,
                                     new_priority=data.get('priority')
                                     )

    feature.title = data.get('title')
    feature.description = data.get('description')
    feature.priority = data.get('priority')
    feature.product_area = data.get('product_area')
    feature.target_date = data.get('target_date')
    feature.client = client

    feature.update()

    return jsonify({'feature': feature_schema.dump(feature).data}), 201


# Delete One particular Feature
@api.route('/feature/<feature_id>', methods=['DELETE'])
def delete_feature(feature_id):
    """Delete the given feature
       param required id
    """

    feature = Feature.query.get_or_404(feature_id)
    feature_title = feature.title
    db.session.delete(feature)
    db.session.commit()
    return jsonify({'message': feature_title + ' Deleted!'}), 200
