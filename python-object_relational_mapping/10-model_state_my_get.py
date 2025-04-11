#!/usr/bin/python3
"""
Prints the State object with the name passed as argument from the database hbtn_0e_6_usa.
Usage: ./4-state_filter.py <username> <password> <database> <state name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Set up database engine
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    # Bind session to the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the state using SQL injection safe filtering
    state = session.query(State).filter(State.name == state_name).first()

    # Print result
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    session.close()
