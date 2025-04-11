#!/usr/bin/python3
"""
Adds the State object “Louisiana” to the database hbtn_0e_6_usa.
Usage: ./5-add_state.py <username> <password> <database>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get credentials and db name
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Set up engine and session
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new State object
    new_state = State(name="Louisiana")

    # Add to session and commit
    session.add(new_state)
    session.commit()

    # Print new state's id
    print(f"{new_state.id}")

    session.close()
