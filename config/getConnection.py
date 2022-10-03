import pymongo

url_local = "mongodb://localhost:27017"
db = 'farm'


class GetCollection:
    def __init__(self, collection):
        self.client = pymongo.MongoClient(url_local)
        self.database = self.client.get_database(db)  # it the same as client[db]
        self.collection = self.database.get_collection(collection)  # it the same as database[collection_name]

    def __enter__(self):
        return self.collection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()
