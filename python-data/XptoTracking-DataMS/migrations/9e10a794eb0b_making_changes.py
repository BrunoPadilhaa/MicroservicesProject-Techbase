"""making changes

Revision ID: 9e10a794eb0b
Revises: f29615ef8ecd
Create Date: 2023-02-28 16:04:39.014887

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9e10a794eb0b'
down_revision = 'f29615ef8ecd'
branch_labels = ()
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('telemetryData',
    sa.Column('data_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('vehicle_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('data_hora', sa.DateTime(length=255), nullable=False),
    sa.Column('latitude', sa.Float(Precision=64), nullable=True),
    sa.Column('longitude', sa.Float(Precision=64), nullable=True),
    sa.Column('altimeter', sa.Integer, nullable=True),
    sa.Column('value', sa.Integer, nullable=True),
    sa.Column('tipo', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('data_id'),

    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('telemetryData')
    # ### end Alembic commands ###
