import unittest
from todclean.use_cases.task.unchecker import TaskUncheck


class TestTaskUnchecker(unittest.TestCase):
    def setUp(self):
        from todclean.repositories.in_memory import InMemory
        from todclean import repo_manager as manager
        self.repo = InMemory()
        manager.save_repo('task', self.repo)

        from todclean.entities.task import Task
        from todclean.use_cases.task.adder import TaskAdd
        from todclean.use_cases.task.checker import TaskCheck
        self.task = Task('test task')
        adder = TaskAdd()
        checker = TaskCheck()
        self.task = adder.add_task(self.task)
        self.task = checker.check_task(self.task.task_id)

        self.unchecker = TaskUncheck()

    def test_task_uncheck(self):
        self.task = self.unchecker.uncheck_task(self.task.task_id)
        self.assertFalse(self.task.done)

    def test_task_uncheck_not_found_raise_error(self):
        with self.assertRaises(KeyError):
            self.task = self.unchecker.uncheck_task(10)
