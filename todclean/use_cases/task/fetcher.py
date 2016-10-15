from todclean import repo_manager as manager


class TaskFetch:

    def __init__(self):
        self.repository = manager('task')

    def fetch_tasks(self):
        return self.repository.all()
