from participant import Participant

class Participants:
    mParticipants: [Participant]

    def __init__(
        participants: [Participant]):
        mParticipants = participants

    def getById(
        id: int):
        if id < len(mParticipants):
            return mParticipants[id]
        return None

    def deleteById(
        id: int):
        del mParticipants[id]
