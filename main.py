import uvicorn
from group import Group
from groups import Groups
from typing import Union
from fastapi import FastAPI

ITEM_NOT_FOUND = "Item not found :("

app = FastAPI(
    docs_url="swagger"
)

groups = Groups([
    Group(1, "asd", "asd"),
    Group(2, "fsdfsdfdsf", "asdsadsadsad")
])

def getParticipants(
    groupId: int):

    group = groups.findById(groupId)

    if group == None:
        return None

    return group.getParticipants()

@app.get("/")
def read_root():
    return "It just not works :( @Todd Howard"

# Python sucks in OOP, sorry dude :)
# CODE BELOW IS F***ING HORRIBLE ASS
# Groups
@app.get("/group/{id}")
def read_groupId(
    id: int):
    group = groups.findById(id)

    if group == None:
        return ITEM_NOT_FOUND
    
    return group.json()

@app.delete("/group/{id}")
def delete_groupId(
    id: int):
    groups.deleteById(id)
    return "{id}Removed"

@app.put("/group/{id}")
def put_groupId(
    id: int,
    name: str,
    description: str):

    group = groups.findById(id)

    if group == None:
        return ITEM_NOT_FOUND

    return {
        "name": group.getName(),
        "description": group.getDescription()
    }

@app.get("/groups")
def read_groups():
    return groups.json()

@app.delete("/group/{groupId}/participant/{participantId}")
def delete_participant(
    groupId: int,
    participantId: int):

    parts = getParticipants()

    if parts == None:
        return ITEM_NOT_FOUND

    parts.deleteById(participantId)

@app.get("/group/{groupId}/participant/{participantId}/recipient")    
def read_recipient(
    groupId: int,
    participantId: int):

    parts = getParticipants(groupId)

    if parts == None:
        return ITEM_NOT_FOUND

    participant = parts.getById(participantId)

    if participant == None:
        return ITEM_NOT_FOUND

    return participant.json()


if __name__ == "__main__":
    uvicorn.run(app, port=8080)