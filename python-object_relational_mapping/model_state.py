"""
Contains the class definition of State and an instance Base = declarative_base()
The script connects to a MySQL server running on localhost at port 3306 using SQLAlchemy.
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Declare the Base class using SQLAlchemy's declarative_base
Base = declarative_base()


class State(Base):
    """
    State class inherits from Base.
    Links to the MySQL table 'states'.
    """

    __tablename__ = 'states'  # Name of the MySQL table

    # Class attributes (columns in the table)
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return f"<State(id={self.id}, name={self.name})>"
