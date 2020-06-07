"""Study area data migration

Revision ID: 0b71a0a4a731
Revises: d89e57b734a5
Create Date: 2020-06-07 19:46:39.781619

"""
import os

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b71a0a4a731'
down_revision = 'd89e57b734a5'
branch_labels = None
depends_on = None


def upgrade():
    with open(os.path.join(os.path.dirname(__file__), '..', 'static/study-area-data.sql'), 'r') as fp:
        for count, line in enumerate(fp):
            op.execute(line)
    pass


def downgrade():
    op.execute('TRUNCATE TABLE study_area RESTART IDENTITY CASCADE;')
    pass
