from todclean import repo_manager as manager


class TaskUncheck:

    def __init__(self):
        self.repository = manager('task')

    def uncheck_task(self, task_id):
        return self.repository.uncheck(task_id)
