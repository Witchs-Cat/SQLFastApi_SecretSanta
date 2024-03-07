from database import Database

class Recipient(Database):

    TABLE_NAME = "Recipients"


    def __init__(self,
        connection: Connection):

        super().__init__(
            dbName,
            self.TABLE_NAME
        )

        pass

    def getRecipientById():
        pass