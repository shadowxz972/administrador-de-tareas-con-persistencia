import sqlite3

from app.classes.task import Task


def connect_db():
    """
    Conecta con la base de datos, si no existe la crea
    :return: None
    """
    with sqlite3.connect('tasks.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS "task" (
                "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                "name" TEXT NOT NULL,
                "deadline" TEXT,
                "description" TEXT,
                "is_completed" INTEGER NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE UNIQUE INDEX IF NOT EXISTS "UNIQUE_id"
            ON "task" ("id")
        ''')
        conn.commit()


def read_db() -> list:
    """
    Retorna una lista con los datos de la base de datos
    :return: lista de tareas
    """
    with sqlite3.connect('tasks.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM task
        ''')
        tareas = cursor.fetchall()
        return tareas


def add_task_to_db(task: Task) -> None:
    """
    Añade una tarea a la base de datos
    :param task:
    :return:
    """
    with sqlite3.connect('tasks.db') as conn:
        cursor = conn.cursor()
        values = (task.name, task.description, task.get_str_date(), task.is_completed)
        cursor.execute('INSERT INTO task (name,description,deadline,is_completed) VALUES (?,?,?,?)', values)
        if not task.id:
            task.id = cursor.lastrowid
        conn.commit()


def update_task_row(task_id: int, update: str, value: str | int) -> None:
    """
    Actualiza un valor de una fila de la base de datos
    :param task_id:
    :param update:
    :param value:
    :return:
    """
    with sqlite3.connect('tasks.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f'UPDATE task SET {update} = ? WHERE id = ?', (value, task_id))
        conn.commit()


def delete_task_row(task_id: int) -> None:
    """
    Borra una fila de la base de datos
    :param task_id:
    :return:
    """
    with sqlite3.connect('tasks.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f'DELETE FROM task WHERE id = ?', (task_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Tarea con id {task_id} eliminada")
        else:
            raise ValueError(f"No se encontró tarea con id {task_id}")
