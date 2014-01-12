from main import *
from birthday import *
from rot13 import *
from signup import *

application = webapp2.WSGIApplication([("/", Main),
                                       ("/unit2/birthday", Birthday),
                                       ("/unit2/thanks", Thanks),
                                       ("/unit2/rot13", Rot13),
                                       ("/unit2/signup", Signup),
                                       ("/unit2/welcome", Welcome)],
                                       debug=True)
