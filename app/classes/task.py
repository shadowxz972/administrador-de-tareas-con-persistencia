from datetime import datetime, date

from app.dtos.taskDTO import TaskDTO
from app.functions.validators import validate_str, validate_date


class Task:
    """
        Maneja la logica de las tareas
    """

    def __init__(self, task_dto: TaskDTO):
        self.__id = task_dto.id
        self.__name = task_dto.name
        self.__description = task_dto.description
        self.__deadline = datetime.strptime(task_dto.deadline, "%d/%m/%Y").date() if task_dto.deadline else None
        self.__is_completed = bool(task_dto.is_completed)

    def __str__(self):
        return f"""
{self.__name}:
    descripcion: {self.__description}
    deadline: {self.__deadline if self.__deadline else "Sin fecha limite"}
    Estado: {"completado" if self.__is_completed else "incompleto"}
"""

    def to_dto(self):
        """
        Retorna un objeto de la clase TaskDTO
        """
        return TaskDTO(id=self.id, name=self.name, description=self.description, deadline=self.get_str_date(),
                       is_completed=int(self.__is_completed))

    def get_str_date(self):
        """
        Retorna la fecha de la tarea en string (formato dd/mm/yyyy)
        """
        if self.__deadline:
            return self.__deadline.strftime("%d/%m/%Y")
        else:
            return self.__deadline

    @property
    def id(self) -> int | None:
        return self.__id

    @id.setter
    def id(self, value: int) -> None:
        if isinstance(value, int):
            self.__id = value
            print("id cambiado correctamente")
        else:
            raise TypeError("el id debe ser un numero entero")

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value) -> None:
        if validate_str(value):
            self.__name = value
            print("Nombre cambiado correctamente")
        else:
            raise TypeError('El nombre debe ser un texto')

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value) -> None:
        if validate_str(value):
            self.__description = value
            print("Descripcion cambiada correctamente")
        else:
            raise TypeError('La descripcion debe ser un texto')

    @property
    def deadline(self) -> date | None:
        return self.__deadline

    @deadline.setter
    def deadline(self, deadline: str | None) -> None:
        if validate_date(deadline):
            self.__deadline = datetime.strptime(deadline, "%d/%m/%Y").date()
            print("Fecha cambiada correctamente")
        elif not deadline:
            self.__deadline = None
        else:
            raise TypeError('La fecha no tiene el formato correcto dd/mm/yyyy')

    @property
    def is_completed(self) -> int | None:
        return self.__is_completed

    @is_completed.setter
    def is_completed(self, value: int | bool) -> None:
        if isinstance(value, (int, bool)):
            self.__is_completed = int(value)
            print("El estado se ha cambiado correctamente")
        else:
            raise TypeError('El estado debe ser un numero entero o un booleano')
