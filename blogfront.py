from handler import *
from post import *
import time

# A front page that lists posts

class BlogFront(Handler):
    def get(self):
        # Retrieve posts from memcache
        posts = top_posts() # front = True)
        # Datastore method to retrieve posts:
        # Post.all().order('-created')
        # GQL method to retrieve posts:
        # posts = db.GqlQuery('select * from Post order by created desc limit 10')
        
        last_queried = int(time.time() - memcache.get('START_TIME'))
        
        if self.format == 'html':
            self.render('front.html', posts = posts, last_queried = last_queried)
        elif self.format == 'json':
            return self.render_json([p.as_dict() for p in posts])
