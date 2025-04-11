#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects from the database hbtn_0e_101_usa.
Usage: ./101-relationship_states_cities.py <username> <password> <database>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City, Base

if __name__ == "__main__":
    # Get database connection parameters from command line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the connection to the database
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )
    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query all states and their cities using the relationship, and order by state id and city id
    states = session.query(State).join(State.cities).order_by(State.id, City.id).all()

    # Loop through all states and their corresponding cities and print in the requested format
    # for state in states:
    #     for city in state.cities:
    #         print(f"{state.name}: ({city.id}) {city.name}")

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    # Close the session
    session.close()
