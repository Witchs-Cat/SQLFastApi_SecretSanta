import sqlite3 as sql
from sqlite3 import Connection
from sqlite3 import Cursor

class Database:

    mConnection: Connection
    mCursor: Cursor

    TABLE_NAME = ""
    QUERY_SELECT_ALL = "*"

    def __init__(
        self,
        dbName: str,
        tableName: str):
        
        self.mConnection = sql.connect(dbName)
        self.TABLE_NAME = tableName
        self.mCursor = self.mConnection.cursor()
        pass

    def create(self,
        fields: str):

        print("create: ", self.mCursor.execute(f"create table if not exists {self.TABLE_NAME} ({fields});"))
        
        pass

    def selectById(self,
        id: int,
        fields: str = QUERY_SELECT_ALL):

        self.mCursor.execute(f"select {fields} from {self.TABLE_NAME} where id={id};")
        return self.mCursor.fetchone()
        

    def insert(self,
        values: str):
        
        self.mCursor.execute(f"insert into {self.TABLE_NAME} values ({values});")
        self.mConnection.commit()
        pass

    def deleteById(self,
        id: int):
        self.mCursor.execute(f"delete from {self.TABLE_NAME} where id={id}")
        self.mConnection.commit()
        pass

    def update(self,
        values: str,
        where: str):
        
        self.mCursor.execute(f"UPDATE {self.TABLE_NAME} SET {values} WHERE {where};")
        self.mConnection.commit()

        pass

    def close(self):
        self.mCursor.close()
        self.mConnection.close()
        pass
