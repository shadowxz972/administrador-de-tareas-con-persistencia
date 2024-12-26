from pydantic import BaseModel
from typing import Optional

# Para la validacion de entrada (crear o actualizar una tarea)
class TaskCreate(BaseModel):
    name: str
    description: str
    deadline: Optional[str] = None  # Puede ser una fecha en formato string o None
    is_completed: Optional[bool] = False  # Puede ser booleano


# Para la respuesta (cuando recuperamos una tarea)
class TaskResponse(BaseModel):
    id: int
    name: str
    description: str
    deadline: Optional[str] = None
    is_completed: bool

