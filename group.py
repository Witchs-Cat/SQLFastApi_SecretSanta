
from participant import Participant
class Group:

    mId: int
    mName: str
    mDescription: str
    mParticipants: [Participant]

    def __init__(self,
        id: int,
        name: str,
        description: str,
        participants: [Participant]):

        mId = id
        mName = name
        mDescription = description
        mParticipants = participants
        
    def json():
        return {
            "id": mId,
            "name": mName,
            "description": mDescription
        }