from handler import *
from post import *
import time

# A permalink page for particular posts

class Permalink(Handler):
    def get(self, post_id):
    	# Create a key for the post with the id: post_id
        key = db.Key.from_path('Post', int(post_id), parent = blog_key())
        post = db.get(key) # Store it in post

        last_queried_permalink = memcache.get('%d' % post.key().id())
        if not last_queried_permalink: # Set time of last query into memcache
            logging.error('DB QUERY POST')
            memcache.set('%d' % post.key().id(), time.time())
            last_queried_permalink = int(time.time() - memcache.get('%d' % post.key().id()))
        else: # Update time of last query
            last_queried_permalink = int(time.time()) - int(last_queried_permalink)

        if not post:
            self.error(404)
            return
        if self.format == 'html':
            self.render('permalink.html', post = post, last_queried_permalink = last_queried_permalink)
        else:
        	self.render_json(post.as_dict())
