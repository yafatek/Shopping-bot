from sanic import Blueprint
from sanic.response import json

users_bp = Blueprint('users_blueprint')


@users_bp.route('/create', methods=['POST'])
async def create(request):
    return json({
        'status': True,
        'message': 'user created Successfully!'
    })
