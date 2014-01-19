from handler import *

class Thanks(Handler):
    def get(self):
        self.response.write("Thanks! That's a totally valid date!")