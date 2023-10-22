from pymongo import MongoClient
from bson.objectid import ObjectId

#TODO: import for your CRUD module
class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, passW, host, port, dataBase, collection):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = user
        PASS = passW
        HOST = host
        PORT = port
        DB = dataBase
        COL = collection
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary 
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Create method to implement the R in CRUD.
    def read(self, rData):
        if rData is not None:
            findings = self.database.animals.find(rData)
            return findings
        else:
            raise Nothing("Nothing Here")

# Create method to implement the U in CRUD.
    def update(self, findData, replaceData):
        try:
            result = self.database.animals.update_many(findData,replaceData)
            return result
        except Exception as e:
            return e
            
# Create method to implement the D in CRUD.
    def delete(self, delData):
        try:
            result = self.database.animals.delete_many(delData)
            return result
        except Exception as e:
            return e