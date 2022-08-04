"""empty message

Revision ID: 1651361309ed
Revises: 
Create Date: 2022-08-04 10:56:09.095354

"""
from alembic import op
import sqlalchemy as sa
from app import db
from models.models import Role, RegisterForms
import time

# revision identifiers, used by Alembic.
revision = '1651361309ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # import asyncio
    
    # def create_table():
    #     op.create_table('roles',
    #     sa.Column('id', sa.Integer(), nullable=False),
    #     sa.Column('name', sa.String(length=50), server_default='', nullable=False),
    #     sa.Column('label', sa.Unicode(length=255), server_default='', nullable=False),
    #     sa.PrimaryKeyConstraint('id'),
    #     sa.UniqueConstraint('name')
    #     )
    #     op.create_table('users',
    #     sa.Column('id', sa.Integer(), nullable=False),
    #     sa.Column('email', sa.Unicode(length=255), server_default='', nullable=False),
    #     sa.Column('email_confirmed_at', sa.DateTime(), nullable=True),
    #     sa.Column('password', sa.String(length=255), server_default='', nullable=False),
    #     sa.Column('is_active', sa.Boolean(), server_default='0', nullable=False),
    #     sa.Column('first_name', sa.Unicode(length=50), server_default='', nullable=False),
    #     sa.Column('last_name', sa.Unicode(length=50), server_default='', nullable=False),
    #     sa.Column('role_id', sa.Integer(), nullable=True),
    #     sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    #     sa.PrimaryKeyConstraint('id'),
    #     sa.UniqueConstraint('email')
    #     )
    
    # def insert(db):
    #     if "roles" in db.metadata.tables.keys():
    #         role_admin = Role(name="Administrador", label="Admin")
    #         role_empleado = Role(name="Empleado", label="Empleado")
    #         db.session.add(role_admin)
    #         db.session.add(role_empleado)
            
    #         db.session.commit()

    # async def insert_data():      
    #     create_table()
    #     insert(db)
    
   
    # asyncio.run(insert_data())

    # ### commands auto generated by Alembic - please adjust! ###
    
    op.create_table('roles',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=50), server_default='', nullable=False),
        sa.Column('label', sa.Unicode(length=255), server_default='', nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
        )
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.Unicode(length=255), server_default='', nullable=False),
        sa.Column('email_confirmed_at', sa.DateTime(), nullable=True),
        sa.Column('password', sa.String(length=255), server_default='', nullable=False),
        sa.Column('is_active', sa.Boolean(), server_default='0', nullable=False),
        sa.Column('first_name', sa.Unicode(length=50), server_default='', nullable=False),
        sa.Column('last_name', sa.Unicode(length=50), server_default='', nullable=False),
        sa.Column('role_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
        )

        
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('roles')
    # ### end Alembic commands ###
