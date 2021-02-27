"""sear_friends_migrate

Revision ID: c7c370a0412b
Revises: e375c5d2429a
Create Date: 2021-02-26 17:18:00.124226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7c370a0412b'
down_revision = 'e375c5d2429a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_connects_from_user_id', table_name='user_connects')
    op.drop_index('ix_user_connects_to_user_id', table_name='user_connects')
    op.drop_table('user_connects')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_connects',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('from_user_id', sa.INTEGER(), nullable=True),
    sa.Column('to_user_id', sa.INTEGER(), nullable=True),
    sa.Column('status', sa.INTEGER(), nullable=True),
    sa.Column('create_at', sa.DATETIME(), nullable=True),
    sa.Column('update_at', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['from_user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['to_user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_user_connects_to_user_id', 'user_connects', ['to_user_id'], unique=False)
    op.create_index('ix_user_connects_from_user_id', 'user_connects', ['from_user_id'], unique=False)
    # ### end Alembic commands ###
