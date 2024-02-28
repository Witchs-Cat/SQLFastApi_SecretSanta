from typing import List
from participant import Participant
class Group:

    mId: int
    mName: str
    mDescription: str
    mParticipants: List[Participant]

    def __init__(self,
        id: int,
        name: str,
        description: str,
        participants: List[Participant] = None):

        self.mId = id
        self.mName = name
        self.mDescription = description
        self.mParticipants = participants
    
    def getParticipants(self):
        return self.mParticipants

    def getName(self):
        return self.mName
    
    def getDescription(self):
        return self.mDescription

    def json(self):
        return {
            "id": self.mId,
            "name": self.mName,
            "description": self.mDescription
        }