from sanic import Sanic
from sanic.response import json

app = Sanic(name='shopping-bot')


@app.route('/api/v1/')
async def index(request):
    return json({
        'status': True,
        'message': 'Access Denied!, Please Contact System Admin!'
    })


app.run(host='127.0.0.1', port=3000, workers=4)
