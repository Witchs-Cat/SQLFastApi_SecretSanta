
from recipient import Recipient

class Participant(Recipient): #Inheritance sucks in Python. Script kiddies
    mRecipient: Recipient

    def __init__(self,
        id: int,
        name: str,
        wish: str,
        recipient: Recipient = None):

        self.mRecipient = recipient

        Recipient.__init__(
            self,
            id= id,
            name= name,
            wish= wish
        )


    def json(self:Recipient):
        return {
            "id": self.mId,
            "name": self.mName,
            "wish": self.mWish,
            "recipient": {
                "id": self.mRecipient.mId
            }
        }

