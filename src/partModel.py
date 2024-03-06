from pydantic import BaseModel

class ParticipantItem(BaseModel):
    name: str
    description: str = None