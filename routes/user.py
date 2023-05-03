from fastapi import APIRouter
from bson import ObjectId, json_util
from data_base.mongoDB import MongoDBConnection
from schemas.user import userEntity, usersEntity
from models.user import User

usersRouter  = APIRouter()
connection = MongoDBConnection.getInstance()
db = connection.get_database()
# Obtiene todos los usuarios registrados
@usersRouter.get("/getAllUsers/")
async def getUsers():
    try:
        return usersEntity(db.Usuario.find())
    except Exception as e:
        print(f'Error al conectar a la base de datos: {e}')

# Obtiene los datos a partir del email y la contraseña, válida el login en el front
@usersRouter.get("/getUser/{email}/{password}")
async def getUser(email: str, password: str):
    try:
        user = db.Usuario.find_one({"email": email, "password": password})
        if user:
            return {
                "_id": str(user["_id"]),
                "name": user["name"],
                "email": user["email"],
                "password": user["password"]
            }
        else:
            return {"message": "Credenciales incorrectas"}
        
    except Exception as e:
        print(f'Error al procesar la solicitud: {e}')

# Crea un nuevo usuario desde el login del front
@usersRouter.post("/newUser")
async def createUser(user: User):
    new_user = dict(user)
    result = db.Usuario.insert_one(new_user)
    return str(result.inserted_id)

