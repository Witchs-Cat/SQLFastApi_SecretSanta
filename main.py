import uvicorn
from fastapi import FastAPI
from group import Group
from groups import Groups
from typing import Union

ITEM_NOT_FOUND = "Item not found :("

app = FastAPI(
    docs_url="/swagger"
)

con = sql.connect("secret.db")
cur = con.cursor()

#cur.execute("create table groups(id Integer, name Text, description Text);")
cur.execute("INSERT INTO groups VALUES (4, 'Daniil', 'MyGroup');")

res = cur.execute("SELECT * from groups;")
print(res.fetchone())

def getGroupById(id: int):
    try:
        return database.getById(id)
    except:
        return None

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
    return getGroupById(id)

@app.delete("/group/{id}")
def delete_groupId(
    id: int):
    try:
        database.deleteById(id)
        return id +" was removed"
    except:
        return ITEM_NOT_FOUND
    
@app.put("/group/{id}")
async def put_groupId(
    id: int,
    name: str,
    description: str):

    group = getGroupById(id)

    print("GROUP CHECK:", group, id, name, description)

    if group is None:
        database.add(id, {
            "name": name,
            "description": description
        })
        return "Successfully added to database"

    print("GROUP UPDATE:", group, id, name, description)

    database.updateById(str(id), {
        "name": name,
        "description": description
    })

    return "Successfully updated in database"

@app.get("/groups")
def read_groups():
    return database.getAll()

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