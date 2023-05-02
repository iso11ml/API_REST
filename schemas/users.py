from fastapi import FastAPI

app  = FastAPI()
word  = 'No'

@app.get("/getAll/")
async def getUser():
    return {"message": "Mi Primer EndPoint", 'testing': word}

