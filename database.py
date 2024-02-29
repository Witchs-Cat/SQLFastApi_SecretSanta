import sqlite3 as sql
from sqlite3 import Connection
from sqlite3 import Cursor

class Database:

    mConnection: Connection
    mCursor: Cursor

    def __init__(
        self,
        dbName: str):
        
        self.mConnection = sql.connect(dbName)
        self.mCursor = self.mConnection.cursor()
        pass

    def create(self,
        table: str,
        fields: str):

        print("create: ", self.mCursor.execute(f"create table if not exists {table} ({fields});"))
        
        pass

    def selectById(self,
        id: int,
        table: str,
        fields: str):

        self.mCursor.execute(f"select {fields} from {table} where id={id};")
        return self.mCursor.fetchone()
        

    def insert(self,
        table: str,
        values: str):
        
        self.mCursor.execute(f"insert into {table} values ({values});")
        self.mConnection.commit()
        pass

    def update(self,
        table: str,
        values: str,
        where: str):
        
        self.mCursor.execute(f"UPDATE {table} SET {values} WHERE {where};")

        pass
