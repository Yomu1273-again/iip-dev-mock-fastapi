from fastapi import FastAPI
from pymongo import MongoClient
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient

app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb://iip-invoices:WdcGSesRG1iEnyrn4axE9H5w0J2uWOJBLOiFhISUxhyTY01zmIyNRzv5UK9E2BCBU7V4lH0GAAoCACDblVjqnA%3D%3D@iip-invoices.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000")
db = client["invoices-db"]
collection = db["shipment-data"]

# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:4200",
    "https://iip-dev-mock-shipment-portal.azurewebsites.net"
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
