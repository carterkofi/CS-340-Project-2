from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # init to connect to mongodb without authentication
        #self.client = MongoClient('mongodb://localhost:28264')
        # init to connect to mongodb with authentication 
        self.client = MongoClient('mongodb://%s:%s@localhost:28264/AAC' % ('aacuser', '123'))
        self.database = self.client['AAC']

# Create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary 
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Read method to implement the R in CRUD. 
    def read_all(self, data):
        if data is not None:
            cursor = self.database.animals.find(data, {'_id':False}) # return a cursor which is a pointer to a list of results (Documents)
            return cursor
        else:
            raise Exception("Nothing to read, because data parameter is empty")
            return False
    
    def read(self, data):
        if data is not None:
            return self.database.animals.find_one(data) # returns only one document as a python dictionary
        else:
            raise Exception("Nothing to read, because data parameter is empty")
            return False
        
# Update method to implement the U in CRUD.
    def update(self, find, replace):
        if find is not None:
            self.database.animals.update(find, replace)  
            return self.database.animals.find()     
        else:
            raise Exception("Nothing to update, because data parameter is empty")
            return False
        
# Delete method to execute the D in CRUD.
    def delete(self,delete):
         if delete is not None:
            self.database.animals.delete(delete)   
            return True          
         else:
            raise Exception("Nothing to delete, because data parameter is empty")
            return False