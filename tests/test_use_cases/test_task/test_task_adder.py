import unittest
from todclean.use_cases.task.adder import TaskAdd


class TestTaskAdd(unittest.TestCase):

    def setUp(self):
        from todclean.repositories.in_memory import InMemory
        from todclean import repo_manager as manager
        manager.save_repo('task', InMemory())

        from todclean.entities.task import Task
        self.task = Task('test task')
        self.task_adder = TaskAdd()

    def test_save_task(self):
        saved = self.task_adder.add_task(self.task)

        self.assertEqual(saved.task_id, 1)
        self.assertEqual(saved.description, self.task.description)
