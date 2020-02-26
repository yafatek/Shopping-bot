import jwt
from sanic import Blueprint
from sanic.response import json

from apis.users.UsersModel import usersModel

users_bp = Blueprint('users_blueprint')


@users_bp.route('/create', methods=['POST'])
async def create(request):
    query = usersModel.insert().values(
        full_name='feras alawadi',
        email='ferasawady@gmail.com',
        phone_number='00905348854120',
    )
    await request.app.db.execute(query)
    return json({
        'status': True,
        'message': 'user created Successfully!',

    })


@users_bp.route('/auth')
async def auth_user(request):
    payload = {
        'some': 'payload',
        'more': 'jwt'
    }
    # 'exp': datetime.utcnow(),
    # 'nbf': datetime.utcnow() * 60,
    # 'iss': 'YafaTek',
    # 'aud': 'Shopping-bot clients'
    encoded_jwt = jwt.encode(payload, 'secret', algorithm='HS256').decode("utf-8")

    return json({
        'status': True,
        'message': 'JWT Token Fetched Successfully!',
        'access_token': encoded_jwt
    })


@users_bp.route('/login')
async def login(request):
    prefixes = ("Bearer", "Token")
    auth_header = request.headers.get("Authorization")

    if auth_header is not None:
        for prefix in prefixes:
            if prefix in auth_header:
                # decode the token.
                decoded = jwt.decode(auth_header.partition(prefix)[-1].strip(), 'secret', algorithms='HS256')
                return json({'authorized ': decoded})
    return json({
        'message': 'Forbidden, Authorization Token is required!'
    })
