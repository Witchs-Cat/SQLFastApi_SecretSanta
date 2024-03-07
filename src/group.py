from typing import List
from database import Database
from participant import Participant

class Group(Database):

    TABLE_NAME ="groups"
    KEY_ID = "id"
    KEY_NAME = "name"
    KEY_DESC = "description"
    KEY_PARTICIPANTS = "participants"
    KEY_TOSS = "toss"

    def __init__(self,
        dbName: str):

        super().__init__(
            dbName,
            self.TABLE_NAME
        )
        
        super().create(
            f"""
                {self.KEY_ID} Integer,
                {self.KEY_NAME} Text,
                {self.KEY_DESC} Text,
                {self.KEY_TOSS} Bit
            """
        )
        
        pass

    def insert(self,
        id: int,
        name: str,
        description: str):
        Database.insert(self,
            f"{id}, \"{name}\", \"{description}\", 0"
        )
        return "Successfully inserted to Database"

    def update(self,
        id: int,
        name: str,
        description: str) -> str:

        content = super().selectById(
            id
        )

        if content is None:
            return "Group not found"

        super().update(
            f"id={id}, name='{name}', description='{description}'",
            f"id={id}"
        )

        return "Successfully updated in Database"

    def selectAllJson(self):
        result = self.selectAll()

        json = []

        for groupId, name, description, _ in result:
            json.append({
                self.KEY_ID:  groupId,
                self.KEY_NAME: name,
                self.KEY_DESC: description
            })

        return json

    def getByGroupId(self,
        groupId: int) -> tuple[int, any]:
        
        content = self.selectById(
            groupId, 
            f"{self.KEY_ID}, {self.KEY_NAME}, {self.KEY_DESC}"
        )

        if content is None:
            return (409, "Group not found")

        return (200, {
            self.KEY_ID: content[0],
            self.KEY_NAME: content[1],
            self.KEY_DESC: content[2]
        })