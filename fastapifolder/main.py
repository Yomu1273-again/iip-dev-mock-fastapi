from fastapi import FastAPI
from pymongo import MongoClient
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient

app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb://iip-invoices-reassign:LjeeXXOSNafE19uXjYiQ9U0nu8MuTUdbgIqpFPUBmyJQa6i56QnVc5ujFF35KOyIewh7CTNEwA4IACDbdjcNAQ==@iip-invoices-reassign.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@iip-invoices-reassign@")
db = client["invoices-db"]
collection = db["shipment-data"]

# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:4200",
    "https://iip-dev-mock-shipment-portal.azurewebsites.net",
    "https://iip-dev-prototype-main.azurewebsites.net"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {}

@app.get("/getAllExtractedItems")
async def read_items():
    collection = db["extraction-data"]
    items = list(collection.find())
    print(items)
    item_object = []
    for item in items:
        item.pop('_id', None)
        item_object.append(item)
    return item_object

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
