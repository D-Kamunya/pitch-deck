"""Rename some pitches columns

Revision ID: e94a169047cd
Revises: d154ba88cf87
Create Date: 2020-09-23 07:40:14.598200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e94a169047cd'
down_revision = 'd154ba88cf87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('pitch_comments_count', sa.Integer(), nullable=True))
    op.add_column('pitches', sa.Column('pitch_downvotes', sa.Integer(), nullable=True))
    op.add_column('pitches', sa.Column('pitch_upvotes', sa.Integer(), nullable=True))
    op.drop_column('pitches', 'comments_count')
    op.drop_column('pitches', 'downvotes')
    op.drop_column('pitches', 'upvotes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('upvotes', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('pitches', sa.Column('downvotes', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('pitches', sa.Column('comments_count', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('pitches', 'pitch_upvotes')
    op.drop_column('pitches', 'pitch_downvotes')
    op.drop_column('pitches', 'pitch_comments_count')
    # ### end Alembic commands ###