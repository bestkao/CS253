import random
from string import letters
import hashlib

from google.appengine.ext import db

# Returns a string of 5 random
# letters using Python's random module and string package.
def make_salt(length = 5):
    return ''.join(random.choice(letters) for x in xrange(length))

# Returns a hashed password of the format:
# HASH(name + pw + salt),salt
# using sha256 and a given name and password
def make_pw_hash(name, pw, salt = None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (salt, h)

# Returns True if a user's password matches its hash.
def valid_pw(name, password, h):
    salt = h.split(',')[0]
    return h == make_pw_hash(name, password, salt)

# Creates the ancestor element to store all the users
def users_key(group = 'default'):
    return db.Key.from_path('users', group)

# Defines the properties of an user datastore entity

class User(db.Model):
    name = db.StringProperty(required = True)
    pw_hash = db.StringProperty(required = True)
    email = db.StringProperty()

    # Declarators: functions that can be called on the User object
    # rather than on individual instances of User objects

    # Looks up a user by id
    @classmethod
    def by_id(cls, uid):
        return cls.get_by_id(uid, parent = users_key())

    # Looks up a user by name
    @classmethod
    def by_name(cls, name):
        u = cls.all().filter('name =', name).get()
        return u

    # Creates a new User object with a given name, password, and email
    @classmethod
    def register(cls, name, pw, email = None):
        pw_hash = make_pw_hash(name, pw)
        return cls(parent = users_key(),
                   name = name,
                   pw_hash = pw_hash,
                   email = email)

    # Returns the user if a valid name, password, and hash is given
    @classmethod
    def login(cls, name, pw):
        u = cls.by_name(name)
        if u and valid_pw(name, pw, u.pw_hash):
            return u