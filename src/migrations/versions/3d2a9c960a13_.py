"""empty message

Revision ID: 3d2a9c960a13
Revises: 
Create Date: 2021-12-19 18:15:07.548947

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d2a9c960a13'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('social_credit_score', sa.Integer(), nullable=False),
    sa.Column('user_level', sa.String(), nullable=False),
    sa.Column('is_rep', sa.Boolean(), nullable=False),
    sa.Column('score_editable', sa.Boolean(), nullable=True),
    sa.Column('short_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
