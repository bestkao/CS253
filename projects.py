from handler import *

# Projects Page

class Projects(Handler):
    def get(self):
        self.render('projects.html')