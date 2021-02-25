"""comment migrate

Revision ID: 76688a53bfb3
Revises: 5c6dff3be701
Create Date: 2021-02-24 16:13:18.274093

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76688a53bfb3'
down_revision = '5c6dff3be701'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('post_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'post_id')
    # ### end Alembic commands ###