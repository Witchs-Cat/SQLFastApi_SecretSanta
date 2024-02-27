import uvicorn
from group import Group
from groups import Groups
from typing import Union
from fastapi import FastAPI

app = FastAPI(
    docs_url="swagger"
)

groups = Groups([
    Group(1, "asd", "asd"),
    Group(2, "fsdfsdfdsf", "asdsadsadsad")
])

@app.get("/")
def read_root():
    return "It just not works :( @Todd Howard"

# Python sucks in OOP, sorry dude :)
# Groups
@app.get("/group/{id}")
def read_groupId(
    id: int):
    return groups.findById(id).json()

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
    return {
        "name": group.mName,
        "description": group.mDescription
    }

@app.get("/groups")
def read_groups():
    return groups.json()

@app.delete("/group/{groupId}/participant/{participantId}")
def delete_participant(
    groupId: int,
    participantId: int):
    groups.findById(groupId).getParticipants().deleteById(participantId)

@app.get("/group/{groupId}/participant/{participantId}/recipient")    
def read_recipient(
    groupId: int,
    participantId: int):

    parts = groups.findById(groupId).getParticipants()
    
    return parts.getById(participantId).json()

if __name__ == "__main__":

    uvicorn.run(app, port=8080)