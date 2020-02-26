from sanic import Blueprint
from sanic.response import json

items_bp = Blueprint('items_bp')


@items_bp.route('/items')
async def index(request):
    # fetching all items from db.
    results = []
    return json({
        'status': True,
        'message': 'items fetched successfully!',
        'results': results
    })


@items_bp.route('/show_item')
async def show(request):
    args = request.raw_args
    return json({
        'status': True,
        'message': 'item Fetched Successfully!',
        'query_args': args.get('id')
    })


@items_bp.route('/create', methods=['POST'])
async def create(request):
    return json({
        'status': True,
        'message': 'item created successfully!'
    })
