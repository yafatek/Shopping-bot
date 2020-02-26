from sanic import Blueprint

from apis.items.ItemsController import items_bp

items_group = Blueprint.group(items_bp, url_prefix="api/v1/items")
