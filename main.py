from handler import *

# This is a basic web app that says "Hello, World!"

class Main(Handler):
    def get(self):
        self.render("index.html", text = "Hello, World!")