"""empty message

Revision ID: 4720edc032c1
Revises: 3bd24395710a
Create Date: 2021-08-10 23:01:39.349364

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4720edc032c1'
down_revision = '3bd24395710a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_book_author', table_name='book')
    op.drop_index('ix_book_categories', table_name='book')
    op.drop_column('book', 'categories')
    op.drop_column('book', 'author')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('author', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True))
    op.add_column('book', sa.Column('categories', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True))
    op.create_index('ix_book_categories', 'book', ['categories'], unique=False)
    op.create_index('ix_book_author', 'book', ['author'], unique=False)
    # ### end Alembic commands ###
