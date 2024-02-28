from typing import List
from group import Group

class Groups:
    mGroups: List[Group]

    def __init__(self,
        groups: List[Group]):
        self.mGroups = groups

    def findById(self,
        id: int):
        if id < len(self.mGroups):
            return self.mGroups[id]
        return None

    def deleteById(self,
        id: int):
        if id < len(self.mGroups):
            del self.mGroups[id]
        return None

    def json(self):
        json = []

        for j in self.mGroups:
            json.append(j.json())

        return json

