#!/usr/bin/python3
"""module for database engine"""


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
        """
    def new(self):
    def save(self):
            """enables saving of session queries, its a commit"""
            
