from handler import *
import logging
import time

from google.appengine.api import memcache
from google.appengine.ext import db

# Defines the value of the blog's parent

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)

# Retrieve posts from memcache

def top_posts(update = False):
    key = 'top_post'
    posts = memcache.get(key)
    if not posts or update:
        logging.error("DB QUERY")

        # GQL query for a list of 10 most recent ascii art entities
        posts = db.GqlQuery('SELECT * '
                           'FROM Post '
#                           'WHERE ANCESTOR IS :1 '
                           'ORDER BY created DESC '
                           'LIMIT 10')
#                           post_key)

        # Create a list on the cursor posts to
        # prevent the running of multiple queries
        posts = list(posts)
        memcache.set(key, posts)

        # Set time of query on front page
        memcache.set('START_TIME', time.time())

    return posts

# Defines the properties of the datastore entity for posts

class Post(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True, indexed = False)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)

    # Renders the blog entry in html, while substituting newlines with line breaks
    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return render_str('post.html', p = self)

    def as_dict(self):
        return {'subject': self.subject,
                'content': self.content,
                'created': self.created.strftime('%c'),
                'last_modified': self.last_modified.strftime('%c')}
