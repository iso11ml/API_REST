from fastapi import FastAPI
import uvicorn
from routes.user import usersRouter
from routes.article import articlesRouter
from routes.comment import commentRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(usersRouter)
app.include_router(articlesRouter) 
app.include_router(commentRouter) 
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


origins = [
    # "http://localhost",
    # "http://localhost:8000",
    # "http://172.25.144.1:8000", 
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

