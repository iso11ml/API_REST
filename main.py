from fastapi import FastAPI
from routes.users import usersRouter

app = FastAPI()

app.include_router(usersRouter)