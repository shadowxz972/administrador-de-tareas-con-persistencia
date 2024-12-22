from app.classes import TaskManager, Task
from app.dtos.taskDTO import TaskDTO
from app.functions.database import add_task_to_db, delete_task_row, read_db, update_task_row
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
    dto = TaskDTO(name=name, description=description, deadline=deadline)
    task_obj = Task(dto)
    manager.add_task(task_obj)
    add_task_to_db(task_obj)


def del_task_helper(manager: TaskManager):
    name = get_valid_name()
    try:
        task_obj = manager.find_task(name)
    except ValueError as e:
        print(e)
        return

    try:
        manager.del_task(task_obj)
        delete_task_row(task_obj.id)
    except ValueError as e:
        print(e)


def update_name_helper(manager: TaskManager):
    new_name = get_valid_name("Ingrese nuevo nombre: ")
    old_name = get_valid_name("Ingrese antiguo nombre: ")
    try:
        manager.rename_key(new_name, old_name)
    except ValueError as e:
        print(e)
        return
    new_task = manager.find_task(new_name)
    new_task.name = new_name
    update_task_row(new_task.id, "name", new_name)


def update_description_helper(manager: TaskManager):
    name = get_valid_name("Ingrese nombre de la tarea: ")
    try:
        task_obj = manager.find_task(name)
    except ValueError as e:
        print(e)
        return
    new_description = get_valid_description("Ingrese nueva descripcion: ")
    task_obj.description = new_description
    update_task_row(task_obj.id, "description", new_description)


def update_deadline_helper(manager: TaskManager):
    name = get_valid_name("Ingrese nombre de la tarea: ")
    try:
        task = manager.find_task(name)
    except ValueError as e:
        print(e)
        return
    new_deadline = get_valid_deadline()
    task.deadline = new_deadline
    update_task_row(task.id, "deadline", new_deadline)


def upload_task_helper(manager: TaskManager):
    tasks = read_db()
    if tasks:
        for task_obj in tasks:
            task_id = task_obj[0]
            task_name = task_obj[1]
            task_deadline = task_obj[2]
            task_description = task_obj[3]
            task_status = task_obj[4]
            dto = TaskDTO(id=task_id, name=task_name, description=task_description, deadline=task_deadline,
                          is_completed=task_status)
            new_task = Task(dto)
            manager.add_task(new_task)


def check_task_helper(manager: TaskManager):
    name = get_valid_name("Ingrese nombre de la tarea: ")
    try:
        task_obj = manager.find_task(name)
    except ValueError as e:
        print(e)
        return
    manager.check_task(task_obj)
    update_task_row(task_obj.id, "is_completed", task_obj.is_completed)
