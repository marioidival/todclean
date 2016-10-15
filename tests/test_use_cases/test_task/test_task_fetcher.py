import unittest
from todclean.use_cases.task.fetcher import TaskFetch


class TestTaskFetch(unittest.TestCase):

    def setUp(self):
        from todclean.repositories.in_memory import InMemory
        from todclean import repo_manager as manager
        self.repo = InMemory()
        manager.save_repo('task', self.repo)

        from todclean.use_cases.task.adder import TaskAdd
        from todclean.entities.task import Task
        adder = TaskAdd()

        for i in range(10):
            adder.add_task(Task('Test Task {}'.format(i)))

        self.fetcher = TaskFetch()

    def test_task_fetch(self):
        self.assertEqual(10, len(self.fetcher.fetch_tasks()))
