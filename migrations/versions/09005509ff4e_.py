"""empty message

Revision ID: 09005509ff4e
Revises: 1106fdbb5e7e
Create Date: 2023-11-04 16:22:17.558966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09005509ff4e'
down_revision = '1106fdbb5e7e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('language',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey')
    )
    op.drop_table('language')
    # ### end Alembic commands ###
