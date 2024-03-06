from pydantic import BaseModel

class ParticipantItem(BaseModel):
    name: str
    wish: str = None