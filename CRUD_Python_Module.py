# Grazioso Salvare Animal Shelter CRUD Module 

from pymongo import MongoClient 
from bson.objectid import ObjectId 
from pymongo.errors import PyMongoError

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # The username and password are passed in when the class is instantiated. 
        # 
        # Connection Variables 
        # 
        USER = username 
        PASS = password 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 
           
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        """Insert a new animal record."""
        if isinstance(data, dict) and data: 
            try:
                # Insert the dictionary as a new MongoDB document.
                self.collection.insert_one(data)  # data should be dictionary
                return True
            except PyMongoError as error:
                print("Create failed:", error)
                return False
        else: 
            return False 

    # Read method to implement the R in CRUD.
    def read(self, query):
        """Return animal records that match the query."""
        if isinstance(query, dict):
            try:
                # Convert the cursor returned by find() into a list.
                results = self.collection.find(query)
                return list(results)
            except PyMongoError as error:
                print("Read failed:", error)
                return []
        else:
            return []
    
    # Update method to implement the U in CRUD.
    def update(self, query, update_data):
        """Update animal records that match the query."""
        if isinstance(query, dict) and isinstance(update_data, dict):
            try:
                # Update all documents that match the query.
                result = self.collection.update_many(
                    query,
                    {"$set": update_data}
                )

                # Return the number of documents that were changed.
                return result.modified_count

            except PyMongoError as error:
                print("Update failed:", error)
                return 0
        else:
            return 0
        
    # Delete method to implement the D in CRUD.
    def delete(self, query):
        """Delete animal records that match the query."""
        if isinstance(query, dict):
            try:
                # Delete all documents that match the query.
                result = self.collection.delete_many(query)

                # Return the number of documents that were deleted.
                return result.deleted_count

            except PyMongoError as error:
                print("Delete failed:", error)
                return 0
        else:
            return 0