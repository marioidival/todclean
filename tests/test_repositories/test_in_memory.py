import unittest

from todclean.repositories.in_memory import InMemory


class TestRepositoryInMemory(unittest.TestCase):
    def setUp(self):
        from todclean.entities.task import Task
        self.task = Task('my test')
        self.in_memory = InMemory()

    def test_save_in_memory(self):
        saved = self.in_memory.save(self.task)

        self.assertEqual(saved.task_id, 1)

    def test_all_in_memory(self):
        self.assertEqual(len(self.in_memory.all()), 0)

        self.task = self.in_memory.save(self.task)
        self.assertEqual(len(self.in_memory.all()), 1)
        self.assertIn(self.task, self.in_memory.all())

    def test_check_task(self):
        self.task = self.in_memory.save(self.task)
        self.task = self.in_memory.check(self.task.task_id)

        self.assertTrue(self.task.done)

    def test_check_task_not_saved(self):
        with self.assertRaises(KeyError):
            self.in_memory.check(1)

    def test_uncheck_task(self):
        self.task = self.in_memory.save(self.task)
        self.task = self.in_memory.check(self.task.task_id)

        self.assertTrue(self.task.done)

        self.task = self.in_memory.uncheck(self.task.task_id)
        self.assertFalse(self.task.done)

    def test_delete_task(self):
        self.task = self.in_memory.save(self.task)
        self.in_memory.delete(self.task.task_id)

        self.assertNotIn(self.task, self.in_memory.all())

    def test_delete_task_not_saved(self):
        with self.assertRaises(KeyError):
            self.in_memory.delete(1)

    def test_find_task(self):
        self.task = self.in_memory.save(self.task)

        self.assertEqual(self.task, self.in_memory.find(self.task.task_id))

    def test_not_found_raise_error(self):
        with self.assertRaises(KeyError):
            self.in_memory.find(1)
