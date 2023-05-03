#!/usr/bin/python3
"""connect database."""
import MySQLdb
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
"""
create
class to relate with
database
"""
if __name__ == "__main__":
    try:
        if sys.argv[3]:
            engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(sys.argv[1], sys.argv[2], sys.argv[3]))

            Base.metadata.create_all(engine)
            Session = sessionmaker(bind=engine)
            session = Session()

            for states in session.query(State).order_by(State.id).all():
                if "a" in states.name:
                    session.delete(states)

            session.commit()
            session.close()
    except MySQLdb.Error:
        pass
