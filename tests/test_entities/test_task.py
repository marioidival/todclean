import unittest

from todclean.entities.task import Task


class TestTask(unittest.TestCase):
    def test_invalid_task_should_raise_attribute_error(self):
        with self.assertRaises(AttributeError):
            task = Task(description='')

        with self.assertRaises(AttributeError):
            task = Task(description=None)

    def test_valid_task(self):
        task = Task('some task')

        self.assertEqual(task.description, 'some task')
        self.assertEqual(task.done, False)
        self.assertEqual(task.task_id, None)
