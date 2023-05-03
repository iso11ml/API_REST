from fastapi import APIRouter
from bson import json_util
from data_base.mongoDB import MongoDBConnection
from schemas.user import userEntity, usersEntity
from models.user import User

usersRouter  = APIRouter()
connection = MongoDBConnection.getInstance()
db = connection.get_database()

@usersRouter.get("/getAllUsers/")
async def getUsers():
    try:
        return usersEntity(db.Employees.find())
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

@usersRouter.post("/newUser")
async def createUser(user: User):
    try:
        new_user = dict(user)
        print(new_user)
    except Exception as e:
        print(f'Error al conectar a la base de datos: {e}')