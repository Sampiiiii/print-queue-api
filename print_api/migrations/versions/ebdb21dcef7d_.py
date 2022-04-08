"""empty message

Revision ID: ebdb21dcef7d
Revises:
Create Date: 2021-12-31 03:32:54.526422

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ebdb21dcef7d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('printers',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('printer_name', sa.String(
                        length=50), nullable=False),
                    sa.Column('printer_type', sa.Enum('ultimaker', 'prusa',
                                                      name='printer_type'), nullable=False),
                    sa.Column('ip', sa.String(length=15), nullable=True),
                    sa.Column('api_key', sa.String(length=50), nullable=True),
                    sa.Column('total_time_printed',
                              sa.Integer(), nullable=True),
                    sa.Column('completed_prints', sa.Integer(), nullable=True),
                    sa.Column('failed_prints', sa.Integer(), nullable=True),
                    sa.Column('total_filament_used',
                              sa.Integer(), nullable=True),
                    sa.Column('days_on_time', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('printer_name')
                    )
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('email', sa.String(length=80), nullable=False),
                    sa.Column('social_credit_score',
                              sa.Integer(), nullable=False),
                    sa.Column('user_level', sa.String(), nullable=False),
                    sa.Column('is_rep', sa.Boolean(), nullable=False),
                    sa.Column('score_editable', sa.Boolean(), nullable=True),
                    sa.Column('short_name', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('maintenance_logs',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('printer_id', sa.Integer(), nullable=False),
                    sa.Column('maintenance_date', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=True),
                    sa.Column('maintenance_info', sa.String(), nullable=False),
                    sa.ForeignKeyConstraint(
                        ['printer_id'], ['printers.id'], ondelete='cascade'),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('maintenance_logs')
    op.drop_table('users')
    op.drop_table('printers')
    # ### end Alembic commands ###