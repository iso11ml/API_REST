from fastapi import APIRouter
from data_base import MongoDBConnection

User = APIRouter()
word  = 'No'

@User.get("/")
async def getUser():
    try:
        conection = MongoDBConnection.getInstance().get_database()
        word = 'Ok'
    except Exception:
        print(f'Conexion Fallida')

    return {"message": "Mi Primer EndPoint"}

