#!/usr/bin/python3
"""module for database engine"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import Base
from models.user import User


class DBstorage:
    """database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """initialization"""
        # {} {} {} {} - name, password, host, database name
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            os.environ.get('ARC_MYSQL_USER'), os.environ.get('ARC_MYSQL_PASSWORD'),
            os.environ.get('ARC_MYSQL_HOST'), os.environ.get('ARC_MYSQL_DB')))

    def all(self):

    def new(self, obj):
        """brand new instancs added"""
        self.__session.add(obj)

    def save(self):
        """saves atm transactions"""
        self.__session.commit()

    def delete(self):
        """method places an instance into the Session’s list of objects to be marked as deleted"""
        self.__session.delete(obj)
        self.save()

    def reload(self):
        """refreshing objects or when ORM lazy load operations occur"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
    
    def close(self):
        """ method is more like a “reset” back to the clean state and not as much like a “database close” method."""
        self.__sesion.close() 
