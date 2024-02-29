class Recipient:

    mId: int
    mName: str
    mWish: str

    def __init__(self,
        id: int,
        name: str,
        wish: str):

        mId = id
        mName = name
        mWish = wish


    def json(self):
        return {
               
        }