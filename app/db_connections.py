import os
from app import app
from bson import ObjectId
from flask_pymongo import PyMongo

mongo = PyMongo(app, uri=os.environ.get("MONGO_URI"))

# Initializing db collection => "img_converter"
db = mongo.db.img_converter

class DataBase:
    def create_data(self, data):
        db.insert_one(data)

    def read_data(self, query):
        fetched_data = db.find(query)
        return fetched_data

    def update_processed_data(self, _id, query):
        updated_data = db.update_one({"_id": ObjectId(_id)}, {"$set": query})
        return updated_data

    def delete_processed_data(self, _id):
        db.delete_one({"_id": ObjectId(_id)})

    def records_count(self, query):
        return db.count_documents(query)