from google.appengine.ext import db

# Defines the properties of an ascii art datastore entity

class Art(db.Model):
    title = db.StringProperty(required = True)
    art = db.TextProperty(required = True, indexed = False)
    created = db.DateTimeProperty(auto_now_add = True)
    coords = db.GeoPtProperty()
