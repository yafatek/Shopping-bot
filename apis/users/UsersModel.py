import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

meta = sa.MetaData()

usersModel = sa.Table(
    'users',
    meta,
    # table Columns.
    sa.Column('id', sa.Integer),
    sa.Column('full_name', sa.String(100), nullable=False),
    sa.Column('email', sa.String(100), nullable=False),
    sa.Column('phone_number', sa.String(16), nullable=False),
    sa.Column('is_active', sa.Boolean, default=False),
    sa.Column('created_at', sa.TIMESTAMP),
    sa.Column('updated_at', sa.TIMESTAMP),
    sa.Column('deleted_at', sa.TIMESTAMP)
)
