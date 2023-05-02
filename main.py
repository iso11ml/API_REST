from fastapi import FastAPI

from data_base.mongoDB import MongoDBConnection

app = FastAPI()

@app.get("/")
async def root():
    try:
        conection = MongoDBConnection.getInstance().get_database()
        word = 'Ok'
    except Exception:
        print(f'Conexion Fallida')
    return {"message": "Hello World", 'Conection': conection}

