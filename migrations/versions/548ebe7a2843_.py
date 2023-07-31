"""empty message

Revision ID: 548ebe7a2843
Revises: 8162f4d8d850
Create Date: 2023-07-31 13:46:12.142831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '548ebe7a2843'
down_revision = '8162f4d8d850'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('climate', sa.String(length=250), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('orbital_period', sa.Integer(), nullable=True),
    sa.Column('rotation_period', sa.Integer(), nullable=True),
    sa.Column('diameter', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    # ### end Alembic commands ###
