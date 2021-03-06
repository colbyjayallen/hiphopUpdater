"""Changed name

Revision ID: 4d54a68fcead
Revises: 5b708c950563
Create Date: 2019-07-29 19:52:00.396367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d54a68fcead'
down_revision = '5b708c950563'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rapper_id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_rapper_id'), 'user', ['rapper_id'], unique=False)
    op.drop_index('ix_signed_up_rapper_id', table_name='signed_up')
    op.drop_table('signed_up')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('signed_up',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('rapper_id', sa.INTEGER(), nullable=False),
    sa.Column('email', sa.VARCHAR(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_signed_up_rapper_id', 'signed_up', ['rapper_id'], unique=False)
    op.drop_index(op.f('ix_user_rapper_id'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
