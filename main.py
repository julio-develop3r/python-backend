from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hola doris buenas noches :D"}


# Ruta para obtener un item por ID
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}


# Ruta para crear un nuevo item
@app.post("/items/")
def create_item(item: dict):
    return {"message": "Item created!", "item": item}


# Ruta para actualizar un item existente
@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    return {"message": "Item updated!", "item_id": item_id, "item": item}


# Ruta para eliminar un item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted!"}
