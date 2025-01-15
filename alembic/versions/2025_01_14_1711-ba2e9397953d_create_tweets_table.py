"""Create tweets table"


Revision ID: ba2e9397953d
Revises: 
Create Date: 2025-01-14 17:11:23.380509

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ba2e9397953d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "tweets",
        sa.Column("id", sa.Integer, primary_key)
        sa.Column("tweet", sa.String(255))
        sa.Column("date", sa.Datetime)
        sa.Column("author", sa.String(255))
        sa.Column("likes", sa.Integer)

    )


def downgrade() -> None:
    op.drop_table("tweets")
