from typing import List
from database import Database

class Group:

    id:int
    name:str
    description:str

    def __init__(self, id:int, name:str, description:str) -> None:
        self.id = id
        self.name = name
        self.description = description

    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
    # def __init__(self):
    #     Database.__init__(
    #         self,
    #         "secret.db")
        
    #     Database.create(self,
    #         self.TABLE_NAME,
    #         f"{self.KEY_ID} Integer, {self.KEY_NAME} Text, {self.KEY_DESC} Text"
    #     )
        
    #     pass

    # def put(self,
    #     id: int,
    #     name: str,
    #     description: str):

    #     Database.insert(self, self.TABLE_NAME, f"{id}, '{name}', '{description}'")

    #     pass

    # def getById(self,
    #     id: int):
        
    #     groupId, name, description = self.selectById(
    #         id,
    #         self.TABLE_NAME,
    #         f"{self.KEY_ID}, {self.KEY_NAME}, {self.KEY_DESC}"
    #     )

    #     return {
    #         self.KEY_ID:  groupId,
    #         self.KEY_NAME: name,
    #         self.KEY_DESC: description
    #     }