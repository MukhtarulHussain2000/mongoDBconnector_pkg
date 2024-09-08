from typing import Any
import os
import pandas as pd
from pymongo.mongo_client import MongoClient
import json
from ensure import ensure_annotations


class mongodb_operation:

     __collection = None
     __database = None

     def __init__(self, client_url:str, database_name:str, collection_name:str=None):
          self.client_url = client_url
          self.database_name = database_name
          self.collection_name = collection_name
            
     def create_client(self):
          client = MongoClient(self.client_url)
          return client

     def create_database(self):
          if mongodb_operation.__database == None:
               client = self.create_client()
               database = client[self.database_name]
               return database

     def create_collection(self, collection=None):
          if mongodb_operation.__collection == None:
               database = self.create_database()
               collection = database[collection]
               return collection

     def insert_record(self, record:dict, collection_name:str):
          if type(record) == list:
               for data in record:
                    if type(data) != dict:
                         raise TypeError("Record must be in the form of dist")
               
               collection = self.create_collection(collection_name)   
               collection.insert_many(record)  
          
          elif type(record) == dict:
               collection = self.create_collection(collection_name)
               collection.insert_one(record)
                    

     def bulk_insert(self, datafile:str, collection_name:str=None):
          self.path = datafile

          if self.path.endswith('.csv'):
               data = pd.read_csv(self.path, encoding='utf-8')

          elif self.path.endswith('.xlsx'):
               data = pd.read_excel(self.path, encoding='utf-8')

          datajson = json.loads(data.to_json(orient='record'))
          collection = self.create_collection()
          collection.insert_many(datajson)