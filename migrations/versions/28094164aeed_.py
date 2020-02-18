"""empty message

Revision ID: 28094164aeed
Revises: 132f33a12b7a
Create Date: 2020-02-18 18:16:26.690425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28094164aeed'
down_revision = '132f33a12b7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('CustomUser')
    op.drop_table('microblog')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('microblog',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='microblog_pkey'),
    sa.UniqueConstraint('email', name='microblog_email_key'),
    sa.UniqueConstraint('username', name='microblog_username_key')
    )
    op.create_table('CustomUser',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"CustomUser_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='CustomUser_pkey'),
    sa.UniqueConstraint('email', name='CustomUser_email_key'),
    sa.UniqueConstraint('username', name='CustomUser_username_key')
    )
    # ### end Alembic commands ###