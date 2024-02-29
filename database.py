import sqlite3 as sql
from sqlite3 import Connection
from sqlite3 import Cursor

class Database:

    mDatabase: Connection
    mCursor: Cursor

    def __init__(
        self,
        dbName: str):
        
        self.mDatabase = sql.connect(dbName)
        self.mCursor = self.mDatabase.cursor()
        pass

    def create(self,
        table: str,
        fields: str):

        self.mCursor.execute(f"create table {table} ({fields});")
        
        pass

    def insert(self,
        table: str,
        values: str):
        
        self.mCursor.execute(f"insert into {table} values ({values});")
        
        pass

    def update(self,
        table: str,
        values: str,
        where: str):
        
        self.mCursor.execute(f"UPDATE {table} SET {values} WHERE {where};")

        pass
