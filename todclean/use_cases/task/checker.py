from todclean import repo_manager as manager


class TaskCheck:

    def __init__(self):
        self.repository = manager('task')

    def check_task(self, task_id):
        return self.repository.check(task_id)
