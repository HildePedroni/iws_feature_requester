from marshmallow import fields

from feature_requester import db, ma


class Feature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    target_date = db.Column(db.String(15), nullable=False)
    product_area = db.Column(db.String(255), nullable=False)
    priority = db.Column(db.Integer, nullable=False, default=1)
    client_id = db.Column(
        db.Integer,
        db.ForeignKey('client.id', ondelete='CASCADE'),
        nullable=False, server_default='0'
    )
    client = db.relationship('Client')

    def save(self):
        db.session.add(self)
        db.session.commit()


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __init__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()


class ClientSchema(ma.Schema):
    class Meta:
        model = Client


class FeatureSchema(ma.ModelSchema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    description = fields.String(required=True)
    target_date = fields.String(required=True)
    product_area = fields.String(required=True)
    priority = fields.Integer(required=True)
    client = fields.Nested(ClientSchema, only=['id', 'name'], required=True)
