from handler import *
from post import *

# The blog's front page that lists all posts

class Blog(Handler):
    def get(self):
        # Retrieve posts from memcache
        posts = top_posts()
        # Datastore method to retrieve posts:
        # Post.all().order('-created')
        # GQL method to retrieve posts:
        # posts = db.GqlQuery('select * from Post order by created desc limit 10')
        
        # Update time of last query
        last_queried = int(time.time() - memcache.get('START_TIME'))
        
        if self.format == 'html':
            self.render('blog.html', posts = posts, last_queried = last_queried)
        elif self.format == 'json':
            return self.render_json([p.as_dict() for p in posts])
