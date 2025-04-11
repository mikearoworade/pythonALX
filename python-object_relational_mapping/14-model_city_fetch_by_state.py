#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa
Displays: <state name>: (<city id>) <city name>
Usage: ./14-model_city_fetch_by_state.py <username> <password> <database>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to database
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Perform inner join between State and City
    results = session.query(City, State).join(State).order_by(City.id).all()

    # Display results
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
