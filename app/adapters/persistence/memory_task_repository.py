from typing import Dict, List, Optional

from app.application.ports.task_repository import TaskRepository
from app.domain.task import Task


class InMemoryTaskRepository(TaskRepository):
  
    def __init__(self) -> None:
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def list_tasks(self) -> List[Task]:
        return list(self._tasks.values())

    def add_task(self, task: Task) -> Task:
        task.id = self._next_id
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        return self._tasks.get(task_id)

    def update_task(self, task: Task) -> Task:
        if task.id is None or task.id not in self._tasks:
            raise KeyError(f"Task with id {task.id} not found")
        self._tasks[task.id] = task
        return task

    def delete_task(self, task_id: int) -> None:
        self._tasks.pop(task_id, None)
