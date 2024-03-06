from pydantic import BaseModel

class GroupItem(BaseModel):
    name: str
    description: str = None