#!/usr/bin/python3
"""connect database."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys 

if __name__ == '__main__':
    # Crear el motor de base de datos y la sesión
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Obtener el objeto State con id igual a 2 utilizando Session.get()
    up_state = session.get(State, 2)

    if up_state:
        up_state.name = 'New Mexico'
        session.commit()

    session.close()
 