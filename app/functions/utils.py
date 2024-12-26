from app.classes import TaskManager
from app.models.Task import Task
from .validators import get_valid_deadline, get_valid_name, get_valid_description


def menu():
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Marcar tarea como completada (o desmarcar)")
    print("4. Actualizar tarea")
    print("5. Mostrar tareas")
    print("6. Salir")
    return input("Ingrese su opcion: ")


def menu_update():
    print("1. Actualizar nombre")
    print("2. Actualizar descripcion")
    print("3. Actualizar fecha limite")
    return input("Ingrese su opcion: ")


def add_task_helper(manager: TaskManager):
    """
    Añade una tarea al manager con sus validaciones
    :param manager:
    """
    name = get_valid_name()
    description = get_valid_description()
    deadline = get_valid_deadline()
    task = Task(name=name, description=description, deadline=deadline)  # esto no puede botar error por las validaciones
    try:
        manager.add_task(task)
    except ValueError as e:
        print(f"Error: {e}")


def del_task_helper(manager: TaskManager):
    """
    Borra una tarea con el nombre
    :param manager:
    :return:
    """
    name = get_valid_name()
    try:
        task_obj = manager.find_task(name)
    except ValueError as e:
        print(e)
        return
    try:
        manager.del_task(task_obj)
    except ValueError as e:
        print(e)


def update_name_helper(manager: TaskManager):
    """
    Actualiza el nombre de una tarea
    :param manager:
    :return:
    """
    new_name = get_valid_name("Ingrese nuevo nombre: ")
    old_name = get_valid_name("Ingrese antiguo nombre: ")
    try:
        task = manager.find_task(old_name)
        if task.name == new_name:
            raise ValueError("Nombre ya existente")
    except ValueError as e:
        print(f"Error: {e}")
        return
    manager.rename_task(task, new_name)


def update_description_helper(manager: TaskManager):
    """
    Actualiza el descripcion de una tarea
    :param manager:
    :return:
    """
    name = get_valid_name("Ingrese nombre de la tarea: ")
    try:
        task_obj = manager.find_task(name)
    except ValueError as e:
        print(e)
        return
    new_description = get_valid_description("Ingrese nueva descripcion: ")
    manager.change_description(task_obj, new_description)


def update_deadline_helper(manager: TaskManager):
    """
    Actualiza la fecha de la tarea
    :param manager:
    :return:
    """
    name = get_valid_name("Ingrese nombre de la tarea: ")
    try:
        task = manager.find_task(name)
    except ValueError as e:
        print(e)
        return
    new_deadline = get_valid_deadline()
    manager.change_deadline(task, new_deadline)


def check_task_helper(manager: TaskManager):
    """
    Cambia el estado de una tarea dependiendo si esta completada o no
    :param manager:
    :return:
    """
    name = get_valid_name("Ingrese nombre de la tarea: ")
    try:
        task_obj = manager.find_task(name)
    except ValueError as e:
        print(e)
        return
    manager.check_task(task_obj)


def show_tasks_helper(manager: TaskManager):
    try:
        manager.show_tasks()
    except ValueError as e:
        print(f"Error: {e}")
