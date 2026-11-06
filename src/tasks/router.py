from fastapi import APIRouter
from src.tasks import controller
task_routes = APIRouter(prefix="/tasks")
def create_task():
    return controller.create_task()