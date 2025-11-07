from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.task import Task


class TaskRepository(ABC):
 

    @abstractmethod
    def list_tasks(self) -> List[Task]:
        ...

    @abstractmethod
    def add_task(self, task: Task) -> Task:
        ...

    @abstractmethod
    def get_task(self, task_id: int) -> Optional[Task]:
        ...

    @abstractmethod
    def update_task(self, task: Task) -> Task:
        ...

    @abstractmethod
    def delete_task(self, task_id: int) -> None:
        ...
