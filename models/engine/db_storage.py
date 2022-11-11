#!/usr/bin/python3
"""module for database engine"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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

        session = Sessionmaker(bind=self.__engine)

    def all(self):

    def new(self):
        """brand new instancs added"""
        self.__session.add
    def save(self):
        """enables saving of session queries, its a commit"""
        self.__ssession.commit
    def delete(self):
        """method places an instance into the Session’s list of objects to be marked as deleted"""
        self.__session.delete
    def reload(self):
        """refreshing objects or when ORM lazy load operations occur"""
    def close(self):
        """ method is more like a “reset” back to the clean state and not as much like a “database close” method."""
        self.__sesion.close        
