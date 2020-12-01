from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client.get_database('chat_api')

def get_data(collection, query={}, project=None):
    return list(db[collection].find(query, project))

def insert_data(collection, data):
    curs = db[collection].insert_one(data)
    return {"_id": curs.inserted_id}

def delete_data(collection, data):
    curs = db[collection].delete_one(data)
    return curs.deleted_count

def update_publication(data, indentifier, collection='publications'):
    curs = db[collection].update_one(
        {"_id": ObjectId(indentifier)},
        {"$push": {"comments":{"$each": data}}}
    )
    return curs.modified_count
