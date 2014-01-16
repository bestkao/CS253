from handler import *

# A blog post datastore object

class Post(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True, indexed = False)
    created = db.DateTimeProperty(auto_now_add = True)
    #last_modified = db.DateTimeProperty(auto_now = True)
