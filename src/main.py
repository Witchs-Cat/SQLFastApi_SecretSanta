import uvicorn
import random as rand
import sqlite3 as sql

from database import Database
from group import Group
from participant import Participant
from partModel import ParticipantItem
from groupModel import GroupItem
from fastapi import FastAPI
from typing import Union

ITEM_NOT_FOUND = "Item not found :("
DATABASE_NAME = "secret.db"

app = FastAPI(
    docs_url="/swagger"
)

# Python sucks in OOP, sorry dude :)
# CODE BELOW IS F***ING HORRIBLE ASS

# 1
@app.post("/group")
def add_group(
    model: GroupItem):

    id = generateId()

    group = Group(
        DATABASE_NAME
    )

    group.insert(
        id,
        model.name,
        model.description
    )

    group.close()
    return id

# 2
@app.get("/groups")
def get_groups():
    
    group = Group(DATABASE_NAME)
    response = group.selectAllJson()
    group.close()

    return response

# 3
@app.get("/group/{id}")
def get_info_by_group_Id(
    id: int):
    
    group = Group(DATABASE_NAME)
    resp = group.getById(id)
    group.close()

    return resp

# 4
@app.put("/group/{id}")
def put_groupId(
    id: int,
    name: str,
    description: str):

    group = Group(DATABASE_NAME)

    response = group.update(
        id,
        name,
        description
    )

    # Вы кто такие? Я вас не звал, идите в другой поток
    group.close()

    return response


# 5
@app.delete("/group/{id}")
def delete_group_Id(
    id: int):
    group = Group(DATABASE_NAME)
    group.deleteById(id)
    group.close()
    return "Group is successfully deleted"
    

# 6
@app.post("/group/{groupId}/participant")
def write_partcipant(
    groupId: int,
    model: ParticipantItem):

    part = Participant(
        DATABASE_NAME
    )

    id = generateId()

    part.insertById(
        id,
        model.name,
        groupId,
        model.wish
    )

    return id

# 7
@app.delete("/group/{groupId}/participant/{participantId}")
def delete_participant(
    groupId: int,
    participantId: int):

    part = Participant(
        DATABASE_NAME
    )

    part.deleteById(
        participantId
    )

    part.close()
    return "Successfully deleted"

# 8
@app.post("/group/{id}/toss")
def create_toss(
    id: int):

    part = Participant(
        DATABASE_NAME
    )
    res = part.toss(
        id
    )
    part.close()
    return res

# 9
@app.get("/group/{groupId}/participant/{participantId}/recipient")    
def read_recipient(
    groupId: int,
    participantId: int):

    return "sadsad"

def generateId() -> int:
    frac = rand.random()
    return frac * 9223372036854775807

if __name__ == "__main__":
    uvicorn.run(app, port=8080)