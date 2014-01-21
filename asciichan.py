from handler import *
from art import *

# This is a blog of ascii art

class AsciiChan(Handler):
    def render_ascii(self, title = "", art = "", error = ""):
        arts = db.GqlQuery("SELECT * FROM Art "
                            "ORDER BY created DESC ")
        self.render("asciichan.html", title = title, art = art, error = error, arts = arts)

    def get(self):
        self.render_ascii()

    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")
        
        if title and art:
            a = Art(title = title, art = art)
            a.put()

            self.redirect("/asciichan")
        else:
            error = "We need both a title and some artwork!"
            self.render_ascii(title, art, error)
