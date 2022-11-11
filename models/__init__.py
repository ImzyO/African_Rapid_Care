#!/usr/bin/python3
"""instantiation"""
from models.base_model import BaseModel
from models.engine.db_storage import DBstorage


database_storage = DBstorage()
database_storage.reload()
