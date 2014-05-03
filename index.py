from handler import *

# This is the main page containing links to my web apps

class Index(Handler):

    def get(self):
        self.render("index.html")