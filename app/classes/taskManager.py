from sqlalchemy.exc import IntegrityError

from app.database.config import SessionLocal
from app.models.Task import Task


class TaskManager:
    """
    Clase que gestiona las operaciones de las tareas en la base de datos.

    Proporciona metodos para añadir, eliminar, modificar, buscar y listar tareas
    en la base de datos. Utiliza SQLAlchemy ORM para interactuar con la base de datos
    y manejar las transacciones.

    Metodos:
        find_task(task_name: str) -> Task:
            Busca una tarea por su nombre.

        add_task(task: Task) -> None:
            Añade una nueva tarea a la base de datos.

        del_task(task: Task) -> None:
            Elimina una tarea de la base de datos.

        check_task(task: Task) -> None:
            Marca o desmarca una tarea como completada.

        show_tasks() -> None:
            Muestra todas las tareas almacenadas en la base de datos.

        rename_task(task: Task, new_name: str) -> None:
            Cambia el nombre de una tarea.

    Atributos:
        session (Session):
            La sesión de SQLAlchemy utilizada para realizar las operaciones de base de datos.
    """

    def __init__(self, session: SessionLocal):
        self.session = session

    def find_task(self, task_name: str) -> Task:
        """
        Busca una tarea por el nombre
        :param task_name:
        :return: Task
        """
        task = self.session.query(Task).filter(Task.name == task_name).first()
        if task:
            return task
        else:
            raise ValueError("No se encontro la tarea")

    def add_task(self, task: Task) -> None:
        """
        Añade una tarea a la base de datos
        :param task:
        :return:
        """
        # Verificar si existe una tarea con el mismo nombre
        existing_task = self.session.query(Task).filter(Task.name == task.name).first()
        if existing_task:
            raise ValueError(f"Ya existe una tarea con el nombre '{task.name}'")

        if task.name.strip() == "":
            raise ValueError("El nombre de la tarea no puede estar vacio")

        # Agregar la tarea a la sesión y hacer commit
        self.session.add(task)
        try:
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise ValueError(f"Error al agregar la tarea '{task.name}' debido a un conflicto de integridad")

    def del_task(self, task: Task) -> None:
        """
        Borra una tarea de la base de datos
        :param task:
        :return:
        """
        task_to_delete = self.session.query(Task).filter(Task.id == task.id).first()
        if task_to_delete:
            self.session.delete(task_to_delete)
            self.session.commit()
        else:
            raise ValueError("No se encontro la tarea que se quiere eliminar")

    def check_task(self, task: Task) -> None:
        """
        Marca o desmarca una tarea como completada
        :param task:
        :return:
        """
        task_to_check = self.session.query(Task).filter(Task.id == task.id).first()
        if task_to_check:
            task_to_check.is_completed = not task_to_check.is_completed
            self.session.commit()
        else:
            raise ValueError("No se encontro la tarea que se quiere marcar como completada")

    def show_tasks(self) -> None:
        """
        Enseña todas las tareas por la consola
        """
        tasks = self.session.query(Task).all()
        if tasks:
            for task in tasks:
                print(task)
        else:
            raise ValueError("Aun no existen tareas")

    def rename_task(self, task: Task, new_name: str) -> None:
        """
        Cambia el nombre de la tarea
        :param task:
        :param new_name:
        """
        # Verifica si ya existe una tarea con ese nombre
        existing_task = self.session.query(Task).filter(Task.name == new_name).first()
        if existing_task:
            raise ValueError(f"Ya existe una tarea con el nombre '{new_name}'")

        task.name = new_name

        # Hacer commit de los cambios
        self.session.commit()

    def change_deadline(self, task: Task, new_deadline: str) -> None:
        task_to_change = self.session.query(Task).filter(Task.id == task.id).first()
        if task_to_change:
            task_to_change.deadline = new_deadline
            self.session.commit()
        else:
            raise ValueError("No se encontro la tarea que se quiere modificar")

    def change_description(self, task: Task, new_description: str) -> None:
        task_to_change = self.session.query(Task).filter(Task.id == task.id).first()
        if task_to_change:
            task_to_change.description = new_description
            self.session.commit()
        else:
            raise ValueError("No se encontro la tarea que se quiere modificar")
