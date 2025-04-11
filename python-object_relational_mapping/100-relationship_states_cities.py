#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco”
Usage: ./100-relationship_states_cities.py <username> <password> <database>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Create California with city San Francisco
    california = State(name="California")
    california.cities = [City(name="San Francisco")]

    session.add(california)
    session.commit()

    session.close()
