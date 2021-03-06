"""empty message

Revision ID: 793716ee8fde
Revises: 0a9fcb2eeea6
Create Date: 2022-01-18 19:24:15.807647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '793716ee8fde'
down_revision = '0a9fcb2eeea6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('maintenance_logs', sa.Column('done_by', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('maintenance_logs', 'done_by')
    # ### end Alembic commands ###
