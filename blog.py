import webapp2
from index import Index
from birthday import Birthday
from thanks import Thanks
from rot13 import Rot13
from signup import Signup
from welcome import Welcome
from asciichan import AsciiChan
from blogfront import BlogFront
from permalink import Permalink
from newpost import NewPost
from cookie import Cookie

app = webapp2.WSGIApplication([('/', Index),
    ('/birthday', Birthday),
    ('/thanks', Thanks),
    ('/rot13', Rot13),
    ('/signup', Signup),
    ('/welcome', Welcome),
    ('/asciichan', AsciiChan),
    ('/blog/?', BlogFront),
    ('/blog/([0-9]+)', Permalink),
    ('/blog/newpost', NewPost),
    ('/cookie', Cookie)
], debug = True)
