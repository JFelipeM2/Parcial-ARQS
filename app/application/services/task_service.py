from typing import List

from app.application.ports.task_repository import TaskRepository
from app.domain.task import Task, TaskFactory, TaskStatus


class TaskService:
  
    def __init__(self, repository: TaskRepository):
        self._repository = repository

    def create_task(self, title: str, status: str) -> Task:
        try:
            status_enum = TaskStatus(status)
        except ValueError:
            raise ValueError("Invalid status. Must be 'pending' or 'done'")

        task = TaskFactory.create(title, status_enum)
        return self._repository.add_task(task)

    def list_tasks(self) -> List[Task]:
        return self._repository.list_tasks()

    def get_task(self, task_id: int) -> Task:
        task = self._repository.get_task(task_id)
        if task is None:
            raise KeyError(f"Task with id {task_id} not found")
        return task

    def update_task(self, task_id: int, title: str, status: str) -> Task:
        task = self.get_task(task_id)

        if not title or not title.strip():
            raise ValueError("Title must not be empty")

        try:
            status_enum = TaskStatus(status)
        except ValueError:
            raise ValueError("Invalid status. Must be 'pending' or 'done'")

        task.title = title.strip()
        task.status = status_enum
        return self._repository.update_task(task)

    def delete_task(self, task_id: int) -> None:
        # Nos aseguramos de que exista antes de borrar
        self.get_task(task_id)
        self._repository.delete_task(task_id)
