from main import ma
from marshmallow import Schema, fields, validate, validates, ValidationError

class UserSchema(Schema):
    user_id = fields.Int(dump_only=True)
    username = fields.String(required=True, validate=validate.Length(min=4))
    email = fields.Email(required=True, validate=validate.Length(min=5))
    password = fields.String(required=True, validate=validate.Length(min=6))

    # @validates("password")
    # def validate_password(self, value):
    #     if not value or not value.strip():
    #         raise ValidationError("Password cannot be empty or just spaces.")

class login(UserSchema):
    email = fields.Email(required=True, validate=validate.Length(min=5))
    password = fields.String(required=True, validate=validate.Length(min=6))