# -*- coding: utf-8 -*-

__author__ = 'Mario Idival'
__email__ = 'marioidival@gmail.com'
__version__ = '0.1.0'


from todclean.use_cases.interfaces.task import ITask
from zope.component import getGlobalSiteManager

app = getGlobalSiteManager()


class GlobalManager:

    def __init__(self):
        self.app = app

    def save_repo(self, name, repo):
        self.app.registerUtility(repo, ITask, name)

    def __call__(self, key):
        return self.app.getUtility(ITask, key)


repo_manager = GlobalManager()
