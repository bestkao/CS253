from handler import *

# A wiki

class Wiki(Handler):
    def get(self):
        self.redirect('/blog')