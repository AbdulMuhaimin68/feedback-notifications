from marshmallow import fields, Schema, validate, validates, ValidationError

class FeedSchema(Schema):
    
    feedback_id = fields.Int(dump_only=True)
    user_email = fields.Email(required=True, validate=validate.Length(min=10))
    message = fields.String(required=True, validate=validate.Length(min = 10))
    