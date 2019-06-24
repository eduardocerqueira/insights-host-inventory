"""empty message

Revision ID: 2d951983fa89
Revises: 
Create Date: 2018-10-31 21:23:07.038176

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2d951983fa89'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'hosts',
        sa.Column('id', postgresql.UUID(), nullable=False),
        sa.Column('account', sa.String(length=10), nullable=True),
        sa.Column('display_name', sa.String(length=200), nullable=True),
        sa.Column('created_on', sa.DateTime(), nullable=True),
        sa.Column('modified_on', sa.DateTime(), nullable=True),
        sa.Column('facts', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column('tags', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column(
            'canonical_facts', postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
        sa.PrimaryKeyConstraint('id'),
    )

    op.create_index('idxaccount', 'hosts', ['account'], unique=False)

    op.create_index('idxinsightsid',
                    'hosts',
                    [sa.text("(canonical_facts ->> 'insights_id')")]
                    )

    op.create_index('idxgincanonicalfacts',
                    'hosts',
                    ['canonical_facts'],
                    postgresql_ops={'canonical_facts': 'jsonb_path_ops'},
                    postgresql_using='gin'
                    )

# ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idxaccount', table_name='hosts')
    op.drop_index('idxinsightsid', table_name='hosts')
    op.drop_index('idxgincanonicalfacts', table_name='hosts')
    op.drop_table('hosts')


# ### end Alembic commands ###
