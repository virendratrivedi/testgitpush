import pymongo
client = pymongo.MongoClient("mongodb+srv://arpit_t:12345@cluster0.ekedees.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d={
    "name":"sudhshu",
    "email":"su@inu.com",
    "surname" : "kumar"
   }
db1 = client["mongotest"]
coll = db1['test']
coll.insert_one(d)