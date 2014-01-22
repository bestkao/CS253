import webapp2

from index import Index

from birthday import Birthday
from thanks import Thanks

from rot13 import Rot13

from cookie import Cookie

from blogfront import BlogFront
from permalink import Permalink
from newpost import NewPost
from register import Register
from login import Login
from logout import Logout
from welcome import Welcome

from asciichan import AsciiChan

app = webapp2.WSGIApplication([('/', Index),
    ('/birthday', Birthday),
    ('/thanks', Thanks),
    ('/rot13', Rot13),
    ('/cookie', Cookie),
    ('/blog/?', BlogFront),
    ('/blog/([0-9]+)', Permalink),
    ('/blog/newpost', NewPost),
    ('/signup', Register),
    ('/login', Login),
    ('/logout', Logout),
    ('/welcome', Welcome),
    ('/asciichan', AsciiChan)
], debug = True)
