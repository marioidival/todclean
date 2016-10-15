"""
Interface para Task Repository

"""
from zope.interface import Interface


class ITask(Interface):

    def all():
        """Return all tasks"""

    def save(task):
        """Save a task"""

    def check(task_id):
        """Mark as complete a task"""

    def uncheck(task_id):
        """Mark as uncomplete a task"""

    def delete(task_id):
        """Delete a task"""

    def find(task_id):
        """Find a task"""
