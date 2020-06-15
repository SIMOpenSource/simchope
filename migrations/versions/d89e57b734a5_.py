"""empty message

Revision ID: d89e57b734a5
Revises: 
Create Date: 2020-06-07 19:42:15.633861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd89e57b734a5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('simconnect_id', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('ranking', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('simconnect_id')
    )
    op.create_table('study_area',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('area_name', sa.String(), nullable=False),
    sa.Column('block', sa.String(), nullable=False),
    sa.Column('level', sa.Integer(), nullable=False),
    sa.Column('_scores', sa.String(), nullable=False),
    sa.Column('table_count', sa.Integer(), nullable=True),
    sa.Column('capacity', sa.Integer(), nullable=True),
    sa.Column('_facilities', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('last_updated', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('score_update',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student', sa.String(), nullable=False),
    sa.Column('study_area', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['student'], ['student.simconnect_id'], ),
    sa.ForeignKeyConstraint(['study_area'], ['study_area.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('score_update')
    op.drop_table('study_area')
    op.drop_table('student')
    # ### end Alembic commands ###
