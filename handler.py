import os
import webapp2
import jinja2

from google.appengine.ext import db

# Sets template directory to 'templates'

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

# A rendering function for datastore objects that don't inherit from Handler

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

# Main handler to provide rendering convenience functions

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        return render_str(template, **params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

# handles whitespace

def render_post(response, post):
    response.out.write('<b>' + post.subject + '</b><br>')
    response.out.write(post.content)