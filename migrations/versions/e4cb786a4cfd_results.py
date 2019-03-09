"""results

Revision ID: e4cb786a4cfd
Revises: e2de49417410
Create Date: 2019-03-03 16:50:16.778427

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4cb786a4cfd'
down_revision = 'e2de49417410'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('competition', sa.Column('results_published', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('competition', 'results_published')
    # ### end Alembic commands ###
