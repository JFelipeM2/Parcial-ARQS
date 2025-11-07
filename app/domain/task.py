from dataclasses import dataclass
from enum import Enum
from typing import Optional


class TaskStatus(str, Enum):
    PENDING = "pending"
    DONE = "done"


@dataclass
class Task:
    id: Optional[int]
    title: str
    status: TaskStatus

    def mark_done(self) -> None:
        self.status = TaskStatus.DONE

    def mark_pending(self) -> None:
        self.status = TaskStatus.PENDING


class TaskFactory:
   
    @staticmethod
    def create(title: str, status: TaskStatus) -> Task:
        if not title or not title.strip():
            raise ValueError("Title must not be empty")

        return Task(
            id=None,
            title=title.strip(),
            status=status,
        )
