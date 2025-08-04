from flask import Blueprint, jsonify
from app.schemas.UserSchema import UserSchema
from app.repository.UserRepo import UserRepository
from webargs.flaskparser import use_args
from sqlalchemy.orm import scoped_session

bp = Blueprint('user', __name__)



@bp.route('/api/user', methods = ['POST'])
@use_args(UserSchema(), location="json")
def add_user(args):
    # breakpoint
    session = UserRepository.get_session()
    user = UserRepository.add_user(args, session = session)
    schema = UserSchema()
    result = schema.dump(user)
    return jsonify({"user" : result})
