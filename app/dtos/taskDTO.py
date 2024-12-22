from dataclasses import dataclass


@dataclass()
class TaskDTO:
    """
    Almacena datos de una tarea
    """
    name: str
    description: str
    deadline: str | None = None
    id: int | None = None
    is_completed: int | bool = 0
