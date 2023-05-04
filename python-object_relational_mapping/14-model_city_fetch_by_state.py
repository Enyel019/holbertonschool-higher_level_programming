#!/usr/bin/python3
"""connect database."""
import MySQLdb
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

"""create class to relate with database."""

if __name__ == "__main__":
    try:
        if sys.argv[3]:
            engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(sys.argv[1], sys.argv[2], sys.argv[3]))

            # Create a session and query the database
            Base.metadata.create_all(engine)
            Session = sessionmaker(bind=engine)
            session = Session()

            for state, city in session.query(State, City).filter(
                    State.id == City.state_id).order_by(City.id).all():
                print("{}: ({}) {}".format(state.name, city.id, city.name))
            session.close()
    except MySQLdb.Error:
        pass
