from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_manager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash
from app.model.User import User
from webargs.flaskparser import use_args
from app.schemas.UserSchema import UserSchema
from app.repository.UserRepo import UserRepository

bp = Blueprint("login", __name__)

@bp.route('/api/login', methods = ['POST'])
@use_args(UserSchema(), location='json')
def login(args):
    session = UserRepository.get_session()
    user = UserRepository.get_through_email(args, session = session)
    if not user or not user.check_password(args['password']):
        return jsonify({'message' : 'Invalid credentials...'})
    access_token =  create_access_token(identity=str(user.user_id))
    return jsonify ({"access_token" : access_token})

@bp.route('/api/protected', methods = ['GET'])
@jwt_required()
def protected():
    user_id = get_jwt_identity()
    breakpoint
    return jsonify({"user" : user_id})