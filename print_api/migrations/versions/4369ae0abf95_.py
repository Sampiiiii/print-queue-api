"""empty message

Revision ID: 4369ae0abf95
Revises: c76037cc2380
Create Date: 2022-04-08 17:08:28.048569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4369ae0abf95'
down_revision = 'c76037cc2380'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('user_score', sa.Integer(), nullable=False))
    op.drop_column('users', 'user_level')
    op.drop_column('users', 'social_credit_score')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('social_credit_score', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('users', sa.Column('user_level', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('users', 'user_score')
    # ### end Alembic commands ###
