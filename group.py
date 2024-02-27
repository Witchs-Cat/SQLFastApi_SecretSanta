
class Group:

    mId: int
    mName: str
    mDescription: str
    mParticipants: [Participant]

    def __init__(self,
        id,
        name,
        description):

        mId = id
        mName = name
        mDescription = description
        
    def json():
        return {
            "id": mId,
            "name": mName,
            "description": mDescription
        }