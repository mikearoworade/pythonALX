#!/usr/bin/python3
"""
Updates the name of the State where id = 2 to 'New Mexico'
Usage: ./6-update_state.py <username> <password> <database>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get credentials and database
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Setup engine and session
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for State with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    session.close()
