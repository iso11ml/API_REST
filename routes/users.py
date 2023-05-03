from fastapi import APIRouter
from bson import json_util
from data_base.mongoDB import MongoDBConnection

usersRouter  = APIRouter()


@usersRouter.get("/getAllUsers/")
async def getUsers():
    try:
        connection = MongoDBConnection.getInstance()
        db = connection.get_database()
        users = db.Employees.find()
        # Convertir los documentos a una lista
        users_json = json_util.dumps(users)
        return {"users": users_json}
    except Exception as e:
        print(f'Error al conectar a la base de datos: {e}')


@usersRouter.get("/getUserPassword/{id}")
async def getUserPassword():
    try:
        connection = MongoDBConnection.getInstance()
        db = connection.get_database() 
        users = db.Employees.find()
        # Convertir los documentos a una lista
        users_json = json_util.dumps(users)
        return {"users": users_json}
    except Exception as e:
        print(f'Error al procesar la solicitud: {e}')

