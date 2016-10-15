from todclean import repo_manager as manager


class TaskAdd:

    def __init__(self):
        self.repository = manager('task')

    def add_task(self, task):
        return self.repository.save(task)
