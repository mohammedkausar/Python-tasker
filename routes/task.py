from fastapi import APIRouter,HTTPException
from typing import List
from models.task_model import Task,TaskInDB
from controller import task_controller

router = APIRouter()

@router.post("/create_task", response_model=TaskInDB)
def create_task(task: Task):
    try:
        return task_controller.create_task(task)
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    
@router.get("/get-all-task", response_model=List[Task])
def get_all_task():
    try:
        return  task_controller.get_all_task()
    except Exception as e:
        raise  HTTPException(status_code=404,detail=str(e))
