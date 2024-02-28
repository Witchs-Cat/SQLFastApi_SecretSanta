import uvicorn
from typing import Union
from fastapi import FastAPI

app = FastAPI(
    docs_url='/swagger'
)

@app.get("/")
def read_root():
    return {"Hello" : "world"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q} 


@app.get("/group/{id}")
def read_groupId(id: int):
    return {
        "id": id
        }

if __name__ == "__main__":
    uvicorn.run(app, port=8080)