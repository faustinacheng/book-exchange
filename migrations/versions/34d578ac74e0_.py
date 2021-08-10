"""empty message

Revision ID: 34d578ac74e0
Revises: 6d68044f25d0
Create Date: 2021-08-10 22:55:07.890970

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '34d578ac74e0'
down_revision = '6d68044f25d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('author', postgresql.ARRAY(sa.String()), nullable=True))
    op.add_column('book', sa.Column('categories', postgresql.ARRAY(sa.String()), nullable=True))
    op.create_index(op.f('ix_book_author'), 'book', ['author'], unique=False)
    op.create_index(op.f('ix_book_categories'), 'book', ['categories'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_book_categories'), table_name='book')
    op.drop_index(op.f('ix_book_author'), table_name='book')
    op.drop_column('book', 'categories')
    op.drop_column('book', 'author')
    # ### end Alembic commands ###
