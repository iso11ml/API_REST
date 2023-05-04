from fastapi import FastAPI
import uvicorn
from routes.user import usersRouter
from routes.article import articlesRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(usersRouter)
app.include_router(articlesRouter) 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)