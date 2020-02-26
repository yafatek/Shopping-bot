from databases import Database
from sanic import Sanic
from sanic.response import json

from apis.items import items_group
from apis.users.__int__ import users_group

app = Sanic(name='shopping-bot')
app.blueprint(users_group)
app.blueprint(items_group)
app.config.DB_URL = 'mysql+pymysql://hinet:12345678@localhost:3306/shopping_bot'
app.db = Database(app.config.DB_URL)


@app.listener('after_server_start')
async def connect_db(*args, **kwargs):
    await app.db.connect()


@app.listener('after_server_stop')
async def disconnect_db(*args, **kwargs):
    await app.db.disconnect()


def setup_database():
    app.db = Database(app.config.DB_URL)


@app.route('/api/v1/')
async def index(request):
    # result = requests.get('https://misafir.app/api/v1/users/show_users')
    return json({
        'status': True,
        'message': 'Access Denied!, Please Contact System Admin!',
    })


app.run(host='127.0.0.1', port=3000, workers=2)
