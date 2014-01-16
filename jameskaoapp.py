from main import Main
from birthday import *
from rot13 import Rot13
from signup import *
from asciichan import *
from blog import Blog
from newpost import NewPost
from permalink import Permalink

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
