from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)

from backend.models.models import db, User

bcrypt = Bcrypt()
jwt = JWTManager()

bp = Blueprint('auth', __name__)


@bp.record_once
def init_ext(state):
    app = state.app
    bcrypt.init_app(app)
    jwt.init_app(app)


@bp.route('/api/auth/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    email = data.get('email')
    password = data.get('password')
    full_name = data.get('full_name')
    if not email or not password or not full_name:
        return jsonify({'error': 'Missing data'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'User already exists'}), 400

    pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    user = User(email=email, password_hash=pw_hash, full_name=full_name)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created'}), 201


@bp.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({'error': 'Missing credentials'}), 400

    user = User.query.filter_by(email=email).first()
    if not user or not bcrypt.check_password_hash(user.password_hash, password):
        return jsonify({'error': 'Invalid credentials'}), 401

    token = create_access_token(identity=user.id)
    return jsonify({'access_token': token})


@bp.route('/api/auth/logout', methods=['POST'])
@jwt_required()
def logout():
    # Token blacklisting not implemented
    return jsonify({'message': 'Logged out'}), 200


@bp.route('/api/auth/me', methods=['GET'])
@jwt_required()
def me():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'id': user.id, 'email': user.email, 'full_name': user.full_name})
