# from helpers.mongo import get_data
from pymongo import MongoClient

client = MongoClient()
db = client.get_database('chat_api')

def get_data(collection, query={}, project=None):
    return list(db[collection].find(query, project))

def collect_comments(collection='publications'):
    project = {
        '_id': 0,
        'comments': 1
    }
    res = list(get_data(collection=collection, project=project))
    return [
        subdic['text']
            for dic in res
                for subdic in dic['comments']
    ]
