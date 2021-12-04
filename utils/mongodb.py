# nagy mennyiségú adatot - dokumentumok tárolására optimalizálták
# horizontálisan scalel - sharding - shardolás
# NoSQL  - nem az sql a lekérdező nyelve
# szakít magával az RDBMS működéssel - relációs adatbázis  
# 
# 
# Erősségek:
# jól találod és építed ki az indexeket, akkor gyakorlatilag nem lesz "table scan" - nem fog a dokumentumok között egyáltalán keresni 
# gyors - ez milyen már :)
# viszonylag jó a dokumentációja
# 
#
# Gyengeségek:
# fenn említett példából kiindulva az index használat
# nincs join - de ugye ez nem is RDBMS
# 
# 

# Gridfs
# CRUD
# Create / insert / upsert 
# Read / select
# Update
# Delete

import pymongo as mongo
from pymongo import collection
from bson import ObjectId

# kapcsolat szintjei
# cliens - ez maga az, hogy kapcsolódunk az adatbázishoz - driveren keresztül
# database-hez kell csatlakozni
# collection-höz akarsz hozzáférni

def get_database():
    uri = 'mongodb://localhost'
    client = mongo.MongoClient(uri)
    database = client['test_database']

    return database

def get_collection(collection_name):
    database = get_database()
    collection = database[collection_name]

    return collection

def get_data_by_id(id):
    collection = get_collection('test_collection')

    return collection.find({"_id": ObjectId(id)})


def read_document():
    collection = get_collection('test_collection')

    # ha mindent le akarok kérni
    # for item in collection.find({}):
    #     print(item)

    # ha egy specifikus adatot akarok lekérni
    # for item in collection.find({"auto": "kék"}):
    #     print(item)
    # like-os keresés1

    # "auto": /p/ -> like '%p%'
    # "auto": /^p/ -> like 'p%'
    # "auto": /p$/ -> like '%p'
    # for item in collection.find({"auto":{'$regex': '^s$'}}): # like '%p%'
    #     print(item)

    return collection.find({})

def insert_document(document):
    collection = get_collection('test_collection')

    ids = collection.insert_one(document).inserted_id

    return ids


def insert_many_documents(documents):
    collection = get_collection('test_collection')

    ids = collection.insert_many(documents).inserted_ids

    return ids

def delete_document(query):
    collection = get_collection('test_collection')    

    return collection.delete_one(query).deleted_count

def delete_many_documents(query):
    collection = get_collection('test_collection')    

    return collection.delete_many(query).deleted_count

def update_document(query):
    collection = get_collection('test_collection')

    # update_one(query-keresési feltétel-{"kulcs":"érték"}, {"$set": {"mező név":"érték"}}), upsert= True/False
    return collection.update_one(query, {"$set":{"type":"sedan"}}, upsert = True).upserted_id

def update_many_docs(query):
    collection = get_collection('test_collection')  

    return  collection.update_many(query, {"$set":{"motor_type":"elektromos"}}, upsert = True).upserted_id


if __name__ == '__main__':
    #con = get_database()
    #print(con)

    get_collection('test_collection')
    data = read_document()

    # for item in data:
    #     print(type(item))
    #     break

    temp_data = {"sütemény": "palacsinta", "leves": "kelkáposzta", "főétel": "rántotthúz rizsával"}

    #print(insert_document(temp_data))

    # for item in get_data_by_id("61a67144a74d399a335af361"):
    #     print(item)

    temp_data = [
        {"sütemény": "palacsinta", "leves": "kelkáposzta", "főétel": "rántotthúz rizsával"},
        {"sütemény": "palacsinta", "leves": "kelkáposzta", "főétel": "rántotthúz rizsával"},
        {"sütemény": "palacsinta", "leves": "kelkáposzta", "főétel": "rántotthúz rizsával"},
        {"sütemény": "palacsinta", "leves": "kelkáposzta", "főétel": "rántotthúz rizsával"},
        {"sütemény": "palacsinta", "leves": "kelkáposzta", "főétel": "rántotthúz rizsával"},
        {"sütemény": "palacsinta", "leves": "kelkáposzta", "főétel": "rántotthúz rizsával"},
        {"sütemény": "palacsinta", "leves": "kelkáposzta", "főétel": "rántotthúz rizsával"},
        {"sütemény": "palacsinta", "leves": "kelkáposzta", "főétel": "rántotthúz rizsával"},
        {"sütemény": "palacsinta", "leves": "kelkáposzta", "főétel": "rántotthúz rizsával"},
        {"sütemény": "palacsinta", "leves": "kelkáposzta", "főétel": "rántotthúz rizsával"},
        {"sütemény": "palacsinta", "leves": "kelkáposzta", "főétel": "rántotthúz rizsával"},
        {"sütemény": "palacsinta", "leves": "kelkáposzta", "főétel": "rántotthúz rizsával"},    
    ]

    ids = insert_many_documents(temp_data)

    print(ids)

    #del_count = delete_document({"sütemény": "palacsinta"})
    

    # del_count = delete_many_documents({"sütemény": "palacsinta"})
    # print(del_count)

    # query = {"auto": "purple"}
    # print(update_document(query))


    # query = {"auto":{'$regex': '^p'}}

    # print(update_may_docs(query))