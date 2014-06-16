from handler import *

# Bootstrap Demo

class Bootstrap(Handler):
    def get(self):
        self.render('bootstrap.html')