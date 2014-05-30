import webapp2

# Main Page
from index import Index

# Projects Page
from projects import Projects

# Lesson Projects
from birthday import Birthday
from thanks import Thanks
from rot13 import Rot13
from cookie import Cookie
from asciichan import AsciiChan

# Blog
from blog import Blog
from permalink import Permalink
from newpost import NewPost
from register import Register
from login import Login
from logout import Logout
from welcome import Welcome
from flush import Flush

# Wiki
from wiki import Wiki

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/projects', Projects),
    # Lesson Projects
    ('/birthday', Birthday),
    ('/thanks', Thanks),
    ('/rot13', Rot13),
    ('/cookie', Cookie),
    ('/asciichan', AsciiChan),
    # Blog
    ('/blog/?(?:\.json)?', Blog),
    ('/blog/([0-9]+)(?:\.json)?', Permalink),
    ('/newpost', NewPost),
    ('/signup', Register),
    ('/login', Login),
    ('/logout', Logout),
    ('/welcome', Welcome),
    ('/flush', Flush),
    ('/wiki', Wiki)
    ], debug = True)
