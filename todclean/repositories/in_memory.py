from todclean.use_cases.interfaces.task import ITask
from zope.interface import implementer


@implementer(ITask)
class InMemory:

    def __init__(self):
        self._data = {}
        self.next_id = 1

    def _do_change(self, task_id, bool_value):
        task = self._data[task_id]
        task.done = bool_value
        self._data[task_id] = task
        return task

    def save(self, task):
        self._data[self.next_id] = task
        task.task_id = self.next_id
        self.next_id += 1
        return task

    def all(self):
        return self._data.values()

    def check(self, task_id):
        return self._do_change(task_id, True)

    def uncheck(self, task_id):
        return self._do_change(task_id, False)

    def delete(self, task_id):
        del self._data[task_id]

    def find(self, task_id):
        return self._data[task_id]
