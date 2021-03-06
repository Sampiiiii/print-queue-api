"""empty message

Revision ID: 34c55fa2a910
Revises: 793716ee8fde
Create Date: 2022-01-21 00:24:49.288155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34c55fa2a910'
down_revision = '793716ee8fde'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auth',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('key', sa.String(), nullable=False),
    sa.Column('date_added', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('associated_version', sa.String(), nullable=True),
    sa.Column('permission_value', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('auth')
    # ### end Alembic commands ###
