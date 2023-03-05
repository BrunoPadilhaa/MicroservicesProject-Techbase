"""making changes

Revision ID: ff92042e2153
Revises: de403f55da04
Create Date: 2023-03-01 11:13:16.660017

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ff92042e2153'
down_revision = 'de403f55da04'
branch_labels = ()
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('telemetryData',
    sa.Column('data_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('vehicle_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('data_hora', sa.DateTime(), nullable=True),
    sa.Column('latitude', sa.Numeric(), nullable=True),
    sa.Column('longitude', sa.Numeric(), nullable=True),
    sa.Column('altimeter', sa.Integer(), nullable=True),
    sa.Column('telemetry_value', sa.Integer(), nullable=True),
    sa.Column('tipo_sensor', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('data_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('telemetryData')
    # ### end Alembic commands ###