"""empty message

Revision ID: 1be0ebb48cda
Revises: f979e7da3f55
Create Date: 2022-10-05 15:41:17.266454

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1be0ebb48cda'
down_revision = 'f979e7da3f55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('question', 'create_time')
    # ### end Alembic commands ###