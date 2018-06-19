from flask import Blueprint, jsonify

api = Blueprint('api', __name__)


@api.route('/feature', methods=['GET'])
def get_all_features():
    return jsonify({'features': 'List of all features'})


@api.route('/feature/<feature_id>', methods=['GET'])
def get_one_feature(feature_id):
    return jsonify({'features': 'One feature'})


@api.route('/feature', methods=['POST'])
def create_new_feature():
    return jsonify({'message': 'new feature created'})


# PATCH Feature
@api.route('/feature/<feature_id>', methods=['PATCH'])
def update_feature(feature_id):
    return 'Updating a particular feature {}'.format(feature_id)


# Delete One particular Feature
@api.route('/feature/<feature_id>', methods=['DELETE'])
def delete_feature(feature_id):
    return 'deleting this feature {}'.format(feature_id)
