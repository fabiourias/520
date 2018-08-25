#!/usr/bin/python3
# encoding: utf-8
from pymongo import MongoClient
from bson.objectid import ObjectId

try:
    client = MongoClient()
    db = client['flask-app']
except Exception as e:
    print("Error: {}".format(e))
    exit()

users = [x for x in db.user.find()]
print(users)

# modificando dados no registro com push
user = db.user.update_one(
    {"_id":ObjectId('5b65b1aae3d0b514d71cda03')},
    {
        "$pull":{
            "mensagens":{
                "nome":"Fabio urias"
                }

            }


    }
)
print(user.matched_count, user.modified_count)

'''
# Alterando com update e set 
user = db.user.update_one(
    {"mensagens.nome":"novousuario"},
    {
        "$set":{
            "mensagens.$.nome":"Daniel"

        }
    }
)


# incluindo dados no registro com push
user = db.user.update_one(
    {"_id":ObjectId('5b65b1aae3d0b514d71cda03')},
    {
        "$push":{
            "mensagens":{
                "nome":"novousuario",
                "mensagem":"novamensagem"}

            }


    }
)

#users = [x for x in db.user.find()]
#print(users)

# deletando registro

user = db.user.delete_one(
    {"_id":ObjectId('5b65a51ee3d0b50d7a0ae064')}
)
print (user.deleted_count)

# encontrar o registro por ID


#print(db.user.find_one())
print (db.user.find_one({"_id":ObjectId('5b65a51ee3d0b50d7a0ae064')}))


********************
# Update registro encontrado - primeiro registro apenas
user = db.user.update_one(
    {  "nome":"daniel Prata"},
    {"$set":{
            "email":"danielprata@outlook.com.br"
    }}
    
)
print(user.matched_count, user.modified_count)

****************
Consulta ou busca
users = db.user.find()
for user in users:
    print(user)

#ou 

users = [x for x in db.user.find()]
print(users)

#print(user["_id"].generation_time)


***********************************************
# Criando o banco no Mongo


db.user.insert_one(
    {
        "nome":"daniel Prata",
        "email":"daniel.prata@4linux.com.br",
        "mensagens":[
            {
                "nome":"usuario",
                "mensagem":"mensagem"
            }
        ]
    }
)
'''