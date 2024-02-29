import uvicorn
from database import Database
from fastapi import FastAPI
from group import Group
from typing import Union

ITEM_NOT_FOUND = "Item not found :("

app = FastAPI(
    docs_url="/swagger"
)

group = Group()

def getParticipants(
    groupId: int):

    group = groups.findById(groupId)

    if group == None:
        return None

    return group.getParticipants()

@app.get("/")
def read_root():
    return "It just not works :(\n@Todd Howard"

# Python sucks in OOP, sorry dude :)
# CODE BELOW IS F***ING HORRIBLE ASS
# Groups
@app.get("/group/{id}")
def read_groupId(
    id: int):
    return group.getById(id)

@app.delete("/group/{id}")
def delete_groupId(
    id: int):
    return "dddd"
    
@app.put("/group/{id}")
async def put_groupId(
    id: int,
    name: str,
    description: str):
    
    group.put(
        id,
        name,
        description
    )
    
    return "Successfully updated in database"

@app.get("/groups")
def read_groups():
    return "groups"

@app.delete("/group/{groupId}/participant/{participantId}")
def delete_participant(
    groupId: int,
    participantId: int):

    pass

@app.get("/group/{groupId}/participant/{participantId}/recipient")    
def read_recipient(
    groupId: int,
    participantId: int):

    return "sadsad"


if __name__ == "__main__":
    uvicorn.run(app, port=8080)