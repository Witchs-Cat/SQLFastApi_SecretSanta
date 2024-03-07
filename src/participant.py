import sqlite3 as sql
from database import Database
from sqlite3 import Connection
from sqlite3 import Cursor

class Participant(Database):

    TABLE_NAME ="parts"
    KEY_ID = "id"
    KEY_NAME = "name"
    KEY_WISH = "wish"
    KEY_GROUP_ID = "groupId"

    def __init__(self,
        dbName: str):

        Database.__init__(
            self,
            dbName,
            self.TABLE_NAME)
        
        self.createPartTable()
        pass

    def insertById(self,
        id: int,
        name: str,
        groupId: int,
        wish: str = None):

        Database.insert(self,
            f"{id}, \"{name}\", \"{wish}\",  \"{groupId}\""
        )
        pass


    def getById(self,
        id: int):

        content = self.selectById(id)        

        if content is None:
            return "null"
        
        partId, name, wish = content

        return {
            self.KEY_ID: partId,
            self.KEY_NAME: name,
            self.KEY_WISH: wish
        }
    
    def toss(self,
        groupId: int):
        
        res = Database.selectAll(self,
            f"groupId={groupId}"
        )

        print("RES:", res)

        json = []

        for partId, name, wish, groupId in res:
            json.append({
                self.KEY_ID: partId,
                self.KEY_NAME: name,
                self.KEY_WISH: wish
            })
            pass

        return json

    def createPartTable(self):
        Database.create(self,
            f"""
                {self.KEY_ID} Integer,
                {self.KEY_NAME} Text,
                {self.KEY_WISH} Text,
                {self.KEY_GROUP_ID} Integer
            """
        )
        pass