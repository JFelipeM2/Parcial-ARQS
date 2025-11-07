from typing import List, Literal

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

from app.adapters.persistence.memory_task_repository import InMemoryTaskRepository
from app.application.services.task_service import TaskService
from app.domain.task import Task


app = FastAPI(
    title="Task API",
    version="1.0.0",
    description="API REST sencilla de gestión de tareas",
)

_repository = InMemoryTaskRepository()
_service = TaskService(_repository)



class TaskCreateDTO(BaseModel):
    title: str = Field(..., min_length=1)
    status: Literal["pending", "done"]


class TaskUpdateDTO(BaseModel):
    title: str = Field(..., min_length=1)
    status: Literal["pending", "done"]


class TaskResponseDTO(BaseModel):
    id: int
    title: str
    status: str

    @staticmethod
    def from_entity(task: Task) -> "TaskResponseDTO":
        return TaskResponseDTO(
            id=task.id,
            title=task.title,
            status=task.status.value,
        )


# Endpoints

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/tasks", response_model=List[TaskResponseDTO])
def list_tasks():
    tasks = _service.list_tasks()
    return [TaskResponseDTO.from_entity(t) for t in tasks]


@app.post("/tasks", response_model=TaskResponseDTO, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreateDTO):
    try:
        task = _service.create_task(title=payload.title, status=payload.status)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return TaskResponseDTO.from_entity(task)


@app.get("/tasks/{task_id}", response_model=TaskResponseDTO)
def get_task(task_id: int):
    try:
        task = _service.get_task(task_id)
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return TaskResponseDTO.from_entity(task)


@app.put("/tasks/{task_id}", response_model=TaskResponseDTO)
def update_task(task_id: int, payload: TaskUpdateDTO):
    try:
        task = _service.update_task(
            task_id=task_id,
            title=payload.title,
            status=payload.status,
        )
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return TaskResponseDTO.from_entity(task)


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    try:
        _service.delete_task(task_id)
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return None
