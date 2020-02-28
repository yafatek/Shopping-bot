import jwt
from sanic import Blueprint
from sanic.response import json

# from apis.users.UsersModel import usersModel
from apis.users.UsersModel import Users
from utils.dbhelper import session

users_bp = Blueprint('users_blueprint')


@users_bp.route('/show_all')
async def demo(request):
    if session is None:
        return json({
            'status': False,
            'message': "can't connect to Database"
        })
    # Users Model Should be Used.
    users = session.query(Users).all()
    if users is None:
        return json({
            'status': False,
            'message': ' Table is Empty!',
            'results': None
        })
    results = []
    for user in users:
        temp = {
            "id": user.id,
            "full_name": user.full_name,
            'email': user.email,
            'is_active': user.is_active,
            'created_at': user.created_at,
            'updated_at': user.updated_at,
            'deleted_at': user.deleted_at,

        }
        results.append(temp)
    # user = dbhelper.db.Table('users', dbhelper.metaData, autoload=True, autoload_with=dbhelper.engine)
    return json({
        'status': True,
        'message': ' users Fetched Successfully!',
        'results': results
    })


@users_bp.route('/create', methods=['POST'])
async def create(request):
    user = Users()
    user.full_name = 'feras Alawadi'
    user.email = 'ferasawady@gmail.com'
    user.phone_number = '00905348854120'
    user.is_active = False

    session.add(user)
    session.commit()

    # query = select([phone_number]).where(
    #     model_db_column == request_column)
    # results = session.execute(query).scalar()
    # result = session.commit()

    # query = session.insert().values(
    #     full_name='feras alawadi',
    #     email='ferasawady@gmail.com',
    #     phone_number='00905348854120',
    # )
    # await request.app.db.execute(query)
    return json({
        'status': True,
        'message': 'user created Successfully!',
        'result': "result"

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
