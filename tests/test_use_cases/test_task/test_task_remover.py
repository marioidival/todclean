import unittest
from todclean.use_cases.task.remover import TaskRemove


class TestTaskRemove(unittest.TestCase):

    def setUp(self):
        from todclean.repositories.in_memory import InMemory
        from todclean import repo_manager as manager
        self.repo = InMemory()
        manager.save_repo('task', self.repo)

        from todclean.entities.task import Task
        from todclean.use_cases.task.adder import TaskAdd
        self.task = Task('test task')
        adder = TaskAdd()
        self.task = adder.add_task(self.task)

        self.task_remover = TaskRemove()

    def test_task_remove(self):
        self.task_remover.remove_task(self.task.task_id)

        self.assertEqual(0, len(self.repo.all()))
