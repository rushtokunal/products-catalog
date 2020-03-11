from utils.validation import ValidateInp
from utils.database import Database


class Product(object):
    def __init__(self):
        self.ValidateInp = ValidateInp()
        self.db = Database()

        self.collection_name = 'products'  # product catalog collection name in mongo DB

        self.fields = {
            "product_id": "string",
            "name": "string",
            "created_by": "string",
            "updated_by": "string"
        }

        #Define the required fields for Create
        self.create_required_fields = ["product_id", "name", "created_by", "updated_by"]

        #Define fields optional for Create
        self.create_optional_fields = []

        #Define the required fields for Update
        self.update_required_fields = ["name", "updated_by"]

        # Fields optional for UPDATE
        self.update_optional_fields = []

    def create(self, product):
        # ValidateInp will throw error if invalid
        self.ValidateInp.validate(product, 
                                  self.fields, 
                                  self.create_required_fields, 
                                  self.create_optional_fields)
        
        res = self.db.insert(product, self.collection_name)
        return "Inserted Id " + res

    def find(self, product):  # find all
        return self.db.find(product, 
                            self.collection_name)

    def find_by_id(self, product_id):
        print('sent id from req ~',product_id)
        return self.db.find_by_id(product_id, self.collection_name)

    def update(self, id, product):
        self.ValidateInp.validate(product, 
                                  self.fields, 
                                  self.update_required_fields, 
                                  self.update_optional_fields)
        return self.db.update(id, product,self.collection_name)

    def delete(self, id):
        return self.db.delete(id, self.collection_name)
