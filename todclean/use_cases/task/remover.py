from todclean import repo_manager as manager


class TaskRemove:

    def __init__(self):
        self.repository = manager('task')

    def remove_task(self, task_id):
        return self.repository.delete(task_id)
