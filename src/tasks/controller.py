from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import Task
from fastapi import HTTPException




def create_task(body, db:Session):
    data = body.model_dump()
    new_task = Task(title =data["title"],description = data["description"],is_completed = data["is_completed"])
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"status":"task craeted"}


def get_tasks(db:Session):
    tasks = db.query(Task)
    return {"ststus":"all task"}

def get_one_task(task_id:int,db:Session):
       one_task = db.query(Task).get(task_id)
       if not one_task:
            raise HTTPException(404, detail ="task id is  incorrect" 
            )
       return {"status" : "task fetched", "data": one_task}

def update_task(body:TaskSchema, task_id:int,db:Session):
     one_task = db.query(Task).get(task_id)
     if not one_task:
            raise HTTPException(404, detail ="task id is  incorrect" )
     body = body.model_dump() # type: ignore
     for field, value in body.items(): # type: ignore
          setattr(one_task,field,value)

     
     
     one_task.title=body.title # type: ignore
     one_task.description=body.description # type: ignore
     one_task.is_completed= body.is_completed # type: ignore

     db.add(one_task)
     db.commit()
     db.refresh(one_task)     
     return {"status":"task updated","data":one_task}


def delete_task(task_id:int, db:Session):
     one_task = db.query(Task).get(task_id)
     if not one_task:
                 raise HTTPException(404, detail ="task id is  incorrect" )
     db.delete(one_task)
     db.commit()
     return{"status":"task deleted"}