from config.getConnection import GetCollection
from bson.objectid import ObjectId
collection_name = 'users'


def get_all():
    with GetCollection(collection_name) as collec:
        cursor = collec.find({})
        return list(cursor)


def save_one(student):
    with GetCollection(collection_name) as connection:
        return connection.insert_one(student)


def delete_student(id):
    with GetCollection(collection_name) as col:
        query = {'_id': ObjectId(id)}
        return col.delete_one(query)


delete_student('6339e1474e6903cb053e5dde')