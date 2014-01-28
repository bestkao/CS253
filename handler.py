import os
import jinja2
import hmac
import webapp2
from user import *
import json

# Sets template directory to 'templates'
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

SECRET = "du.uyX(fE~Tb6.pp&U3D-0smY0,Gqi$^jS34tzu9"

# A rendering function for datastore objects that don't inherit from Handler
def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

# Takes a string and returns a string of the format: 
# s|HASH, where HASH is hashed using HMAC and a secret key
def make_secure_val(val):
    return '%s|%s' % (val, hmac.new(SECRET, val).hexdigest())

# Takes a string of the format: h|HASH
# and returns h if hash_str(h) == HASH, otherwise None 
def check_secure_val(secure_val):
    val = secure_val.split('|')[0]
    if secure_val == make_secure_val(val):
        return val

# Main handler to provide rendering convenience functions

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        params['user'] = self.user
        return render_str(template, **params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_json(self, d):
        json_txt = json.dumps(d)
        self.response.headers['Content-Type'] = 'application/json; charset = UTF-8'
        self.write(json_txt)

    # Sets the cookie with a given name and value
    def set_secure_cookie(self, name, val):
        cookie_val = make_secure_val(val)
        self.response.headers.add_header(
            'Set-Cookie',
            '%s=%s; Path=/' % (name, cookie_val))

    # Returns the cookie's value if it passes check_secure value
    def read_secure_cookie(self, name):
        cookie_val = self.request.cookies.get(name)
        return cookie_val and check_secure_val(cookie_val)

    # Sets the cookie's user id to the user's key
    def login(self, user):
        self.set_secure_cookie('user_id', str(user.key().id()))

    # Sets the cookie's user_id to the empty string
    def logout(self):
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')

    # Checks if the user is logged in at every page
    def initialize(self, *a, **kw):
        webapp2.RequestHandler.initialize(self, *a, **kw)
        uid = self.read_secure_cookie('user_id') # Check for the user's cookie value
        self.user = uid and User.by_id(int(uid)) # Store in the user object if it exists

        if self.request.url.endswith('.json'):
            self.format = 'json'
        else:
            self.format = 'html'

# Handles whitespace
def render_post(response, post):
    response.out.write('<b>' + post.subject + '</b><br>')
    response.out.write(post.content)