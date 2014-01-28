import webapp2

# Main Page
from index import Index

# Lesson Projects
from birthday import Birthday
from thanks import Thanks
from rot13 import Rot13
from cookie import Cookie
from asciichan import AsciiChan

# Blog
from blogfront import BlogFront
from permalink import Permalink
from newpost import NewPost
from register import Register
from login import Login
from logout import Logout
from welcome import Welcome

app = webapp2.WSGIApplication([('/', Index),
    # Lesson Projects
    ('/birthday', Birthday),
    ('/thanks', Thanks),
    ('/rot13', Rot13),
    ('/cookie', Cookie),
    ('/asciichan', AsciiChan),
    # Blog
    ('/blog/?(?:\.json)?', BlogFront),
    ('/blog/([0-9]+)(?:\.json)?', Permalink),
    ('/newpost', NewPost),
    ('/signup', Register),
    ('/login', Login),
    ('/logout', Logout),
    ('/welcome', Welcome)
], debug = True)
