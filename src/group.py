from typing import List
from database import Database
from participant import Participant

class Group(Database):

    TABLE_NAME ="groups"
    KEY_ID = "id"
    KEY_NAME = "name"
    KEY_DESC = "description"
    KEY_PARTICIPANTS = "participants"

    def __init__(self,
        dbName: str):

        Database.__init__(
            self,
            dbName,
            self.TABLE_NAME)
        
        Database.create(self,
            f"""
                {self.KEY_ID} Integer,
                {self.KEY_NAME} Text,
                {self.KEY_DESC} Text
            """
        )
        
        pass

    def insert(self,
        id: int,
        name: str,
        description: str):
        Database.insert(self,
            f"{id}, \"{name}\", \"{description}\""
        )
        return "Successfully inserted to Database"

    def update(self,
        id: int,
        name: str,
        description: str) -> str:

        content = Database.selectById(
            self,
            id
        )

        if content is None:
            return "Group not found"

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

    def getParticipantsById(self,
        id: int):

        parts = Participant(
            self.mConnection,
            self.mCursor
        )

        json = []

        for id, name, wish, partId in parts.selectAll(f"groupId={id}"):
            json.append({
                parts.KEY_ID: id,
                parts.KEY_NAME: name,
                parts.KEY_WISH: wish
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
            self.KEY_DESC: description,
            self.KEY_PARTICIPANTS: self.getParticipantsById(
                groupId
            )
        }