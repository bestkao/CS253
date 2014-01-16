from handler import *
from blog import Post

# This is a form to submit new entries and direct them to a permalink after submission

class NewPost(Handler):
    def render_newpost(self, subject = "", content = "", error = ""):
        self.render("newpost.html", subject = subject, content = content, error = error)

    def get(self):
        self.render_newpost()

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")
        
        if subject and content:
            p = Post(subject = subject, content = content)
            p.put()
            self.redirect("/blog/%d" % p.key().id())
        else:
            error = "subject and content, please!"
            self.render_newpost(subject, content, error)
