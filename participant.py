
from participant import Participant
from recipient import Recipient

class Participant(Recipient): #Inheritance sucks in Python. Script kiddies

    mRecipients: Recipient

    def __init__(self,
        id: int,
        name: str,
        wish: str,
        recipient: Recipient):

        mRecipient = recipient

        Recipient.__init__(
            self,
            id= id,
            name= name,
            wish= wish
        )


    def json():
        return {
            "id": mId,
            "name": mName,
            "wish": mWish,
            "recipient": {
                "id": mRecipient.mId
            }
        }

