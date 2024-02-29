from sqlite3 import Connection
from typing import List

from models.group import Group
from collection import BaseCollection

class Groups(BaseCollection):
    def __init__(self,
        db: Connection):
        super().__init__(db, "groups", Group.__annotations__)        

    def getById(self, id: int):
        pass

    def put(self, group: Group):
        self.insert(group.to_json())
