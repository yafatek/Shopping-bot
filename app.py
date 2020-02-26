from sanic import Sanic
from sanic.response import json

from apis.users.__int__ import users_group


app = Sanic(name='shopping-bot')
app.blueprint(users_group)


@app.route('/api/v1/')
async def index(request):
    # result = requests.get('https://misafir.app/api/v1/users/show_users')
    return json({
        'status': True,
        'message': 'Access Denied!, Please Contact System Admin!',
    })


app.run(host='127.0.0.1', port=3000)
