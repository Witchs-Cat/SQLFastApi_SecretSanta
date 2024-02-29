from typing import List
from group import Group

class Groups:
    mGroups: List[Group]

    def __init__(self,
        groups: List[Group]):
        self.mGroups = groups

    def geJson(self):
        json = []

        for j in self.mGroups:
            json.append(j.json())

        return json