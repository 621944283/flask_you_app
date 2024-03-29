"""empty message

Revision ID: f9a4788671eb
Revises: 6b71ce5d5134
Create Date: 2022-08-16 09:26:42.421155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9a4788671eb'
down_revision = '6b71ce5d5134'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('field', sa.Column('description_field', sa.String(length=240), nullable=False))
    op.add_column('field', sa.Column('icon', sa.String(length=25), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('field', 'icon')
    op.drop_column('field', 'description_field')
    # ### end Alembic commands ###
