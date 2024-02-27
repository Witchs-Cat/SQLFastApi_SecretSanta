from group import Group

class Groups:
    mGroups: [Group]

    def __init__(self,
        groups: [Group]):
        mGroups = groups

    def findById(
        id: int):
        return mGroups[id]

    def deleteById(
        id: int):
        del mGroups[id]

    def json():
        json = []

        for j in mGroups:
            json.append(j.json())

        return json

