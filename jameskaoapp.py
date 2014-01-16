from main import *
from birthday import *
from rot13 import *
from signup import *
from asciichan import *
from blog import *
from newpost import *

app = webapp2.WSGIApplication([
	("/", Main),
    ("/birthday", Birthday),
    ("/thanks", Thanks),
    ("/rot13", Rot13),
    ("/signup", Signup),
    ("/welcome", Welcome),
    ("/asciichan", AsciiChan),
    ("/blog", Blog),
    ("/blog/newpost", NewPost),
    ("/blog/(\d+)", Permalink)
	], debug=True)
