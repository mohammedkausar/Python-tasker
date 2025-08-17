from fastapi import FastAPI
from routes import task,auth

app = FastAPI()
app.include_router(task.router, prefix="/task", tags=["Tasks"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])