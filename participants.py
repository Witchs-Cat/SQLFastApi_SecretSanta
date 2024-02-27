from participant import Participant

class Participants:
    mParticipants: [Participant]

    def __init__(
        participants: [Participant]):
        mParticipants = participants

    def getById(
        id: int):
        return mParticipants[id]

    def deleteById(
        id: int):
        del mParticipants[id]
