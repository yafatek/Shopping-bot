"""create users table

Revision ID: 801f5172765c
Revises: 6700550b05f9
Create Date: 2020-02-26 16:34:27.245231

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '801f5172765c'
down_revision = '6700550b05f9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('full_name', sa.String(100), nullable=False),
        sa.Column('phone_number', sa.String(16), nullable=False),
        sa.Column('description', sa.Unicode(200))
    )


def downgrade():
    op.drop_table('users')
