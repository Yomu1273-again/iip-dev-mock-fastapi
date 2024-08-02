from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb+srv://yogeshmuneese:yogeshmuneese@cluster1.bqp7ddk.mongodb.net/")
db = client["IIP_TEST"]
collection = db["SHIPMENT_DETAILS"]

@app.get("/")
def read_root():
    return {}

@app.get("/getAllItems")
async def read_items():
    items = list(collection.find())
    print(items)
    item_object = []
    for item in items:
        item.pop('_id', None)
        item_object.append(item)
    return item_object

@app.put("/insertItem")
async def insert_item(item: dict):
    collection.insert_one(item)
    return {"status": "Item Inserted"}