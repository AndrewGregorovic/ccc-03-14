"""author

Revision ID: bb7a4f287a74
Revises: f27e020415b6
Create Date: 2020-11-14 10:19:57.319540

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb7a4f287a74'
down_revision = 'f27e020415b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('auther', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'auther')
    # ### end Alembic commands ###
