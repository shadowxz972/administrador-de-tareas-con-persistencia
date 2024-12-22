from . import Task


class TaskManager:
    def __init__(self):
        self.__tasks: dict[str, Task] = dict()

    def add_task(self, task: Task) -> None:
        if task.name in self.__tasks:
            raise ValueError(f"Ya existe una tarea con el nombre '{task.name}'")
        if not isinstance(task, Task):
            raise ValueError("El objeto que se quiere agregar no es una tarea")
        if task.name.strip() == "":
            raise ValueError("El nombre de la tarea no puede estar vacio")

        self.__tasks[task.name] = task

    def del_task(self, task: Task) -> None:
        if task.name in self.__tasks:
            del self.__tasks[task.name]
        else:
            raise ValueError("No se encontro la tarea que se quiere eliminar")

    def check_task(self, task: Task) -> None:
        if task.name in self.__tasks:
            task.is_completed = not task.is_completed
        else:
            raise ValueError("No se encontro la tarea que se quiere marcar como completada")

    def show_tasks(self) -> None:
        if self.__tasks.values():
            for task in self.__tasks.values():
                print(task)
        else:
            raise ValueError("Aun no existen tareas")

    def find_task(self, task_name: str) -> Task:
        if task_name in self.__tasks:
            return self.__tasks[task_name]
        else:
            raise ValueError("No se encontro la tarea")

    def rename_key(self, new_key: str, old_key: str) -> None:
        if old_key not in self.__tasks:
            raise ValueError("No existe la llave")

        if new_key in self.__tasks:
            raise ValueError("La nueva llave ya existe")

        if new_key == old_key:
            raise ValueError("Las llaves son iguales")

        self.__tasks[new_key] = self.__tasks.pop(old_key)
