from fastapi import APIRouter, HTTPException
from bson import ObjectId
from data_base.mongoDB import MongoDBConnection
from schemas.user import  usersEntity
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

# @usersRouter.get("/getUser/{email}/{password}", response_model = User)
# async def getUser(email: str, password: str):
#     # Verificando errores: Esto es lo que recibe
#     print(f"Email: {email}, Password: {password}")
#     try:
#         user = db.Usuario.find_one({"email": email, "password": password})
#         if user:
#             return userEntity(user)
#         else:
#             raise HTTPException(status_code = 400, detail = "Credenciales incorrectas")
        
#     except Exception as e:
#         print(f'Error al procesar la solicitud: {e}')

@usersRouter.get("/getUser/{email}/{password}", response_model=User)
async def get_user(email: str, password: str):
    try:
        user = db.Usuario.find_one({"email": email, "password": password})
        if user:
            user_dict = dict(user)
            user_dict['idObject'] = str(user_dict.pop('_id'))
            return User(**user_dict)
        else:
            raise HTTPException(status_code=400, detail="Credenciales incorrectas")
    except Exception as e:
        print(f'Error al procesar la solicitud: {e}')

# Obtiene el nombre del usuario a partir del email
@usersRouter.get("/getName/{id}", response_model=str)
async def get_name(id: str):
    user = db.Usuario.find_one({"_id": ObjectId(id)})
    if user:
        return user["name"]
    return " "

# Crear un nuevo usuario
# @usersRouter.post("/newUser", response_model = User)
# async def createUser(user: User):
#     new_user = dict(user)
#     existing_user = db.Usuario.find_one({"email": new_user["email"]})
#     if existing_user:
#         raise HTTPException(status_code = 400, detail = "El correo electrónico ya está en uso")
#     result = db.Usuario.insert_one(new_user)
#     created_user = new_user.copy()
#     created_user["_id"] = str(result.inserted_id)
#     return created_user

@usersRouter.post("/newUser", response_model=User)
async def create_user(user: User):
    print("Ok")
    new_user = dict(user)
    existing_user = db.Usuario.find_one({"email": new_user["email"]})
    if existing_user:
        raise HTTPException(status_code=400, detail="El correo electrónico ya está en uso")
    result = db.Usuario.insert_one(new_user)
    created_user = new_user.copy()
    created_user["idObject"] = str(result.inserted_id)
    return created_user

# Obtiene el id del usuario a partir del email
@usersRouter.get("/getUserIDByEmail/{email}", response_model=str)
async def get_user_id_by_email(email: str):
    user = db.Usuario.find_one({"email": email})
    if user:
        return str(user["_id"])
    else:
        raise HTTPException(status_code=404, detail="User not found")