from typing import List
from database import Database

class Group(Database):

    TABLE_NAME ="groups"
    KEY_ID = "id"
    KEY_NAME = "name"
    KEY_DESC = "description"

    def __init__(self,
        dbName: str):

        Database.__init__(
            self,
            dbName,
            self.TABLE_NAME)
        
        Database.create(self,
            f"{self.KEY_ID} Integer, {self.KEY_NAME} Text, {self.KEY_DESC} Text"
        )
        
        pass

    def put(self,
        id: int,
        name: str,
        description: str) -> str:

        content = Database.selectById(
            self,
            id
        )

        if content is None:
            Database.insert(self,
                f"{id}, '{name}', '{description}'"
            )
            return "Successfully inserted to Database"

        Database.update(self,
            f"id={id}, name='{name}', description='{description}'",
            f"id={id}")

        return "Successfully updated in Database"

    def selectAllJson(self):
        result = self.selectAll()

        json = []

        for groupId, name, description in result:
            json.append({
                self.KEY_ID:  groupId,
                self.KEY_NAME: name,
                self.KEY_DESC: description
            })

        return json

    def getById(self,
        id: int):
        
        content = self.selectById(
            id,
            f"{self.KEY_ID}, {self.KEY_NAME}, {self.KEY_DESC}"
        )

        if content is None:
            return "Item not found"

        groupId, name, description = content

        return {
            self.KEY_ID:  groupId,
            self.KEY_NAME: name,
            self.KEY_DESC: description
        }