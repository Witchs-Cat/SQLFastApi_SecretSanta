import uvicorn
import sqlite3 as sql
from database import Database
from fastapi import FastAPI
from group import Group
from typing import Union

ITEM_NOT_FOUND = "Item not found :("
DATABASE_NAME = "secret.db"

app = FastAPI(
    docs_url="/swagger"
)

# Python sucks in OOP, sorry dude :)
# CODE BELOW IS F***ING HORRIBLE ASS
# Groups
@app.get("/group/{id}")
def read_groupId(
    id: int):
    
    group = Group(DATABASE_NAME)
    resp = group.getById(id)
    group.close()

    return resp

@app.delete("/group/{id}")
def delete_groupId(
    id: int):
    group = Group(DATABASE_NAME)
    group.deleteById(id)
    group.close()
    return "Group is successfully deleted"
    
@app.put("/group/{id}")
def put_groupId(
    id: int,
    name: str,
    description: str):

    group = Group(DATABASE_NAME)

    response = group.put(
        id,
        name,
        description
    )

    # Вы кто такие? Я вас не звал, идите в другой поток
    group.close()

    return response

@app.get("/groups")
def read_groups():
    
    group = Group(DATABASE_NAME)
    response = group.selectAllJson()
    group.close()

    return response

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

@app.get("/")
def read_root():
    return "It just not works :(\n@Todd Howard"

if __name__ == "__main__":
    uvicorn.run(app, port=8080)