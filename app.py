import requests
from sanic import Sanic
from sanic.response import json

app = Sanic(name='shopping-bot')


@app.route('/api/v1/')
async def index(request):
    result = requests.get('https://misafir.app/api/v1/users/show_users')

    return json({
        'status': True,
        'message': 'Access Denied!, Please Contact System Admin!',
        'results': result.json()
    })


app.run(host='127.0.0.1', port=3000, workers=4)
