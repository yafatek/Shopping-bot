# import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()


# meta = sa.MetaData()


class Users(base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True)
    full_name = Column('full_name', String(100), nullable=False)
    email = Column('email', String(100), nullable=False, unique=True)
    phone_number = Column('phone_number', String(16), nullable=False, unique=True)
    is_active = Column('is_active', Boolean)
    created_at = Column('created_at', TIMESTAMP, server_default=text('NOW()'))
    updated_at = Column('updated_at', TIMESTAMP)
    deleted_at = Column('deleted_at', TIMESTAMP)

# usersModel = sa.Table(
#     'users',
#     meta,
#     # table Columns.
#     sa.Column('id', sa.Integer),
#     sa.Column('full_name', sa.String(100), nullable=False),
#     sa.Column('email', sa.String(100), nullable=False),
#     sa.Column('phone_number', sa.String(16), nullable=False),
#     sa.Column('is_active', sa.Boolean, default=False),
#     sa.Column('created_at', sa.TIMESTAMP),
#     sa.Column('updated_at', sa.TIMESTAMP),
#     sa.Column('deleted_at', sa.TIMESTAMP)
# )
