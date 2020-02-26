"""create items table

Revision ID: 6700550b05f9
Revises: 
Create Date: 2020-02-26 16:32:57.226752

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy import text

# revision identifiers, used by Alembic.
revision = '6700550b05f9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'items',
        sa.Column('id', sa.String(200), primary_key=True),
        sa.Column('item_name', sa.String(200), nullable=False),
        sa.Column('category_id', sa.Integer, nullable=False),
        sa.Column('description', sa.Unicode(1000)),
        sa.Column('price', sa.Float, nullable=False),
        sa.Column('created_at', sa.TIMESTAMP, server_default=text('NOW()')),
        sa.Column('updated_at', sa.TIMESTAMP),
        sa.Column('deleted_at', sa.TIMESTAMP)
    )


def downgrade():
    pass
