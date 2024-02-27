
from participant import Participant
from recipient import Recipient

class Participant(Recipient):
    
    mRecipients: [Recipient]

    def __init__(self,
        id: int,
        name: str,
        wish: str,
        recipients: [Recipient]):

        mId = id
        mName = name
        mWish = wish
        mRecipients = recipients


    def json():
        return {

        }

