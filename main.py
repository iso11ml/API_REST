from fastapi import FastAPI
from routes.user import usersRouter
from routes.article import articlesRouter

app = FastAPI()

app.include_router(usersRouter)
app.include_router(articlesRouter) 