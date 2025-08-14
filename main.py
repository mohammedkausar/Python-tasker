from fastapi import FastAPI
from routes import task

app = FastAPI()
app.include_router(task.router, prefix="/task", tags=["Tasks"])