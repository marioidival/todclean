from todclean.use_cases.interfaces.task import ITask
from zope.interface import implementer


@implementer(ITask)
class InMemory:

    def __init__(self):
        self._data = {}
        self.next_id = 1

    def save(self, task):
        self._data[self.next_id] = task
        task.task_id = self.next_id
        self.next_id += 1
        return task

    def all(self):
        return self._data.values()

    def check(self, task_id):
        task = self._data[task_id]
        task.done = True
        self._data[task_id] = task
        return task

    def uncheck(self, task_id):
        task = self._data[task_id]
        task.done = False
        self._data[task_id] = task
        return task

    def delete(self, task_id):
        del self._data[task_id]

    def find(self, task_id):
        return self._data[task_id]
