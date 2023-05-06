from fastapi import APIRouter, HTTPException
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

@usersRouter.get("/getUser/{email}/{password}", response_model = User)
async def getUser(email: str, password: str):
    # Verificando errores: Esto es lo que recibe
    print(f"Email: {email}, Password: {password}")
    try:
        user = db.Usuario.find_one({"email": email, "password": password})
        if user:
            return userEntity(user)
        else:
            raise HTTPException(status_code = 400, detail = "Credenciales incorrectas")
        
    except Exception as e:
        print(f'Error al procesar la solicitud: {e}')

# Crear un nuevo usuario
@usersRouter.post("/newUser", response_model = User)
async def createUser(user: User):
    new_user = dict(user)
    existing_user = db.Usuario.find_one({"email": new_user["email"]})
    if existing_user:
        raise HTTPException(status_code = 400, detail = "El correo electrónico ya está en uso")
    result = db.Usuario.insert_one(new_user)
    created_user = new_user.copy()
    created_user["_id"] = str(result.inserted_id)
    return created_user

