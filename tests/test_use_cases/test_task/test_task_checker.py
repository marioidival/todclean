import unittest
from todclean.use_cases.task.checker import TaskCheck


class TestTaskCheck(unittest.TestCase):

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

        self.task_checker = TaskCheck()

    def test_task_check(self):
        self.task = self.task_checker.check_task(self.task.task_id)
        self.assertTrue(self.task.done)

    def test_task_check_not_found_raise_error(self):
        with self.assertRaises(KeyError):
            self.task = self.task_checker.check_task(10)
