from fastapi import FastAPI
from fastapi import HTTPException ## Used for error handling
from pydantic import BaseModel ## Import BaseModel from Pydantic

app = FastAPI()

## Create an empty list of itesm for the Todo application

## Extend the BaseModel to create an item class

class Item(BaseModel):
    text: str ## Not specifying a default value will make it a mandatory field and this field will be validated for existence by 
    ## the pydantic model.
    is_done: bool = False

items = []

## Define a path for root path "/"
## Use @ app decorator to define the HTTP GET method

@app.get("/")
def root():
    return {"Hello": "World"}

## Use Routes to define various URLs to which you want the application to respond to

## Create endpoint for creating items in the Todo app

@app.post("/items", response_model=list[Item])
def create_item(item: Item): ## item is passed as a query parameter when it is a single data type like int or string or boolean
    ## For a Modelled data type like this Item, we have to pass it as a body or the payload
    items.append(item)
    return items

## Endpoint to view items in the list
## Provide the position(index) of the item. Endpoint will return value of item at the index
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items) and item_id > 0:
        return items[item_id]
    else:
        if item_id < 0:
            raise HTTPException(status_code=404, detail=f"Item not found for negative item_id : {item_id}")
        else:
            raise HTTPException(status_code=404, detail=f"Item {item_id} not found.")
        
## Endpoint to get the list of all the items
## limit query parameter is used to return first n items from the list
@app.get("/items")
def list_items(limit: int=10):
    return items[0:limit]
        
        



