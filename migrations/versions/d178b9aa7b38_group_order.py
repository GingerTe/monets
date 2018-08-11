"""group order

Revision ID: d178b9aa7b38
Revises: 2ab54cce5c31
Create Date: 2018-08-11 17:20:58.542934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd178b9aa7b38'
down_revision = '2ab54cce5c31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('coin_group', sa.Column('order', sa.Integer(), server_default='0', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('coin_group', 'order')
    # ### end Alembic commands ###
