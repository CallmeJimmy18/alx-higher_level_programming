#!/usr/bin/python3
"""
prints the State object with the name passed as argument from the database
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    statinpt = sys.argv[4]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).filter(State.name.like(statinpt,))
    try:
        print(instance[0].id)
    except IndexError:
        print("Not found")
