#!/usr/bin/python3
""" class definition of a State """
from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base


mymeta = MetaData()
Base = declarative_base(metadata=mymeta)


class State(Base):
    """ Representation of a state """
    __tablename__ = 'states'

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
