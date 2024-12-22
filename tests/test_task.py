import unittest

from app.classes.task import Task
from app.dtos.taskDTO import TaskDTO


class TestTask(unittest.TestCase):
    def test_void_name(self):
        with self.assertRaises(TypeError):
            task = Task(TaskDTO(name='test', description='test'))
            task.name = ""

    def test_wrong_name(self):
        with self.assertRaises(TypeError):
            task = Task(TaskDTO(name='test', description='test'))
            task.name = 12

    def test_correct_name(self):
        task = Task(TaskDTO(name='test', description='test'))
        task.name = "carlos"
        self.assertEqual(task.name, task.name)

    def test_void_description(self):
        with self.assertRaises(TypeError):
            task = Task(TaskDTO(name='test', description='test'))
            task.description = ""

    def test_wrong_description(self):
        with self.assertRaises(TypeError):
            task = Task(TaskDTO(name='test', description='test'))
            task.description = 10

    def test_correct_description(self):
        task = Task(TaskDTO(name='test', description='test'))
        task.description = "nueva descripcion"
        self.assertEqual(task.description, task.description)

    def test_wrong_deadline(self):
        task = Task(TaskDTO(name='test', description='test', deadline="10/11/2024"))
        task.deadline = "60/40/2021"
        self.assertEqual(task.deadline, None)

    def test_correct_deadline(self):
        task = Task(TaskDTO(name='test', description='test', deadline="10/11/2024"))
        task.deadline = "17/09/2021"
        self.assertEqual(task.get_str_date(), "17/09/2021")

    def test_to_dto(self):
        task = Task(TaskDTO(id=1, name='test', description='test', deadline="10/11/2024"))
        dto = task.to_dto()
        self.assertEqual(dto, TaskDTO("test", "test", "10/11/2024", 1, 0))

    def test_wrong_is_completed(self):
        with self.assertRaises(TypeError):
            task = Task(TaskDTO(name='test', description='test'))
            task.is_completed = "xddd"

    def test_correct_is_completed(self):
        task = Task(TaskDTO(name='test', description='test'))
        task.is_completed = True
        self.assertTrue(task.is_completed)

    def test_wrong_id(self):
        with self.assertRaises(TypeError):
            task = Task(TaskDTO(name='test', description='test'))
            task.id = "test"

    def test_correct_id(self):
        task = Task(TaskDTO(name='test', description='test'))
        task.id = 10
        self.assertEqual(task.id, 10)


if __name__ == '__main__':
    unittest.main()
