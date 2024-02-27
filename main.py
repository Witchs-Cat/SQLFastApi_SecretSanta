import uvicorn
from group import Group
from groups import Groups
from typing import Union
from fastapi import FastAPI

app = FastAPI()

groups = Groups([
    Group(1, "asd", "asd"),
    Group(2, "fsdfsdfdsf", "asdsadsadsad")
])

@app.get("/")
def read_root():
    return "It just not works :( @Todd Howard"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q} 

@app.get("/group/{id}")
def read_groupId(id: int):
    return groups.findById(id).json()

@app.get("/groups")
def read_groups():
    return groups.json()

if __name__ == "__main__":

    uvicorn.run(app, port=8080)