"""Change date_of_birth to Date

Revision ID: d21e87cbf76d
Revises: 41879a2d584a
Create Date: 2024-05-31 13:28:30.317183

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd21e87cbf76d'
down_revision: Union[str, None] = '41879a2d584a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
