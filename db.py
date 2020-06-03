from flask import Flask
from flask_pymongo import pymongo
from app import app

CONNECTION_STRING = "mongodb+srv://Ceslovas:Microsoftsux1984@cookbook-jqvqs.mongodb.net/radio-stations?retryWrites=true&w=majority"

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('cookbook')
user_collection = pymongo.collection.Collection(db, 'user_collection')