from datetime import datetime
from typing import Optional

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates

from app.database.config import Base, engine
from app.functions.validators import validate_str, validate_date


def validate_string_field(value: str, field_name: str) -> str:
    if validate_str(value):
        print(f"{field_name} cambiado correctamente")
        return value
    else:
        raise TypeError(f'El {field_name} debe ser un texto')


class Task(Base):
    """
    Representa una tarea en la base de datos.

    La clase `Task` interactúa con la tabla `tasks` en la base de datos y proporciona
    la estructura de datos para las tareas. Incluye atributos como el nombre, descripción,
    fecha límite (deadline) y estado de la tarea (completada o no). Además, incluye validaciones
    para los campos y métodos para convertir el campo de fecha en formato `date`.

    Atributos:
        id (int):
            Identificador único de la tarea.
        name (str):
            Nombre de la tarea (único y no nulo).
        description (str):
            Descripción de la tarea (no nulo).
        deadline (Optional[str]):
            Fecha límite de la tarea en formato dd/mm/yyyy (opcional).
        is_completed (int):
            Estado de la tarea (0 = incompleta, 1 = completada).

    Métodos:
        __str__() -> str:
            Representación en formato legible de la tarea.

        __repr__() -> str:
            Representación más técnica para debugging de la tarea.

        deadline_to_date() -> Optional[datetime.date]:
            Convierte la fecha límite de la tarea en un objeto `date`.

        validate_name(key: str, value: str) -> str:
            Valida que el nombre de la tarea sea un texto adecuado.

        validate_description(key: str, value: str) -> str:
            Valida que la descripción de la tarea sea un texto adecuado.

        validate_deadline(key: str, value: Optional[str]) -> Optional[str]:
            Valida que la fecha límite tenga el formato correcto `dd/mm/yyyy`.

        validate_is_completed(key: str, value: int | bool) -> int:
            Valida que el estado de la tarea sea un valor booleano o un número entero.

    Excepciones:
        TypeError:
            Si los valores de los atributos no cumplen con los formatos o restricciones establecidos.
    """
    __tablename__ = 'tasks'

    # Usamos un solo guion bajo para evitar el name mangling
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)
    deadline = Column(String, nullable=True, default=None)
    is_completed = Column(Integer, nullable=False, default=0)

    def __str__(self):
        return f"""
{self.name}:
    descripcion: {self.description}
    deadline: {self.deadline if self.deadline else "Sin fecha limite"}
    Estado: {"completado" if self.is_completed else "incompleto"}
"""

    def __repr__(self):
        return f"<Task(id={self.id}, name={self.name}, description={self.description}, deadline={self.deadline}, is_completed={self.is_completed})>"

    def deadline_to_date(self) -> Optional[datetime.date]:
        """
        Retorna el deadline en objeto date
        """
        if validate_date(self.deadline):
            self.deadline = datetime.strptime(self.deadline, "%d/%m/%Y").date()
        elif not self.deadline:
            self.deadline = None
        else:
            raise TypeError('La fecha no tiene el formato correcto dd/mm/yyyy')

    @validates("name")
    def validate_name(self, key: str, value: str) -> str:
        return validate_string_field(value, 'nombre')

    @validates("description")
    def validate_description(self, key: str, value: str) -> str:
        return validate_string_field(value, 'descripcion')

    @validates("deadline")
    def validate_deadline(self, key: str, value: Optional[str]) -> Optional[str]:
        if validate_date(value):
            return value
        elif not value:
            return None
        else:
            raise TypeError('La fecha no tiene el formato correcto dd/mm/yyyy')

    @validates("is_completed")
    def validate_is_completed(self, key: str, value: int | bool) -> int:
        if isinstance(value, (int, bool)):
            return int(value)
        else:
            raise TypeError('El estado debe ser un numero entero o un booleano')


# creamos las tablas en la base de datos
Base.metadata.create_all(bind=engine)
