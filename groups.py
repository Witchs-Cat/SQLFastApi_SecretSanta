from group import Group

class Groups:
    mGroups: [Group]

    def __init__(self,
        groups: [Group]):
        mGroups = groups

    def findById(
        id: int):
        if id < len(mGroups):
            return mGroups[id]
        return None

    def deleteById(
        id: int):
        if id < len(mGroups):
            del mGroups[id]
        return None

    def json():
        json = []

        for j in mGroups:
            json.append(j.json())

        return json

