#!/usr/bin/python3
"""instantiation"""
from models.base_model import BaseModel
from models.engine.db_storage import DBstorage
from models.user import User


database_storage = DBstorage()
database_storage.reload()
