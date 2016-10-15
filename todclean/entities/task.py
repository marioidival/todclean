

class Task:

    def __init__(self, description):
        if not description:
            raise AttributeError

        self._id = None
        self._done = False
        self.description = description

    @property
    def task_id(self):
        return self._id

    @task_id.setter
    def task_id(self, id):
        self._id = id

    @property
    def done(self):
        return self._done

    @done.setter
    def done(self, value):
        self._done = value
