from handler import *
from post import *
# import time

# A permalink page for particular posts

class Permalink(Handler):
    def get(self, post_id):
    	# Create a key for the post with the id: post_id
        key = db.Key.from_path('Post', int(post_id), parent = blog_key())
        post = db.get(key) # Store it in post

        # last_queried = int(time.time() - memcache.get('START_TIME'))

        if not post:
            self.error(404)
            return
        if self.format == 'html':
            self.render('permalink.html', post = post) #, last_queried = last_queried)
        else:
        	self.render_json(post.as_dict())
