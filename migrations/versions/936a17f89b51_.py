"""empty message

Revision ID: 936a17f89b51
Revises: ea8d83b3bfe4
Create Date: 2021-08-10 22:14:26.593818

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '936a17f89b51'
down_revision = 'ea8d83b3bfe4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(length=30), nullable=False))
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_column('user', 'username')
    # ### end Alembic commands ###
