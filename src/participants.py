from typing import List
from participant import Participant

class Participants:
    mParticipants: List[Participant]

    def __init__(
        participants: List[Participant]):
        mParticipants = participants

    def getById(self,
        id: int):
        if id < len(self.mParticipants):
            return self.mParticipants[id]
        return None

    def deleteById(self,
        id: int):
        del self.mParticipants[id]
