import os
import sys

# Para solucionar un bug de importacion
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(current_dir, '..')
sys.path.append(project_root)

from app.classes import TaskManager
from app.classes import TaskManager
from app.functions.utils import menu, add_task_helper, del_task_helper, upload_task_helper, menu_update, \
    update_name_helper, update_deadline_helper, update_description_helper, check_task_helper


def main():
    manager = TaskManager()

    upload_task_helper(manager)

    while True:
        option = menu()
        os.system('cls' if os.name == 'nt' else 'clear')
        match option:
            case "1":
                add_task_helper(manager)
            case "2":
                del_task_helper(manager)
            case "3":
                check_task_helper(manager)
            case "4":
                option = menu_update()
                match option:
                    case "1":
                        update_name_helper(manager)
                    case "2":
                        update_description_helper(manager)
                    case "3":
                        update_deadline_helper(manager)
                    case _:
                        print("Opcion invalida, intente denuevo")
            case "5":
                manager.show_tasks()
            case "6":
                print("Saliendo...")
                break
            case _:
                print("Opcion invalida")


if __name__ == '__main__':
    main()
