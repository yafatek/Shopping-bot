from sanic import Blueprint

from apis.users.UsersController import users_bp

users_group = Blueprint.group(users_bp, url_prefix='api/v1/users')
