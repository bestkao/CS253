from handler import *
from post import *

# A front page that lists posts

class BlogFront(Handler):
    def get(self):
    	  posts = top_posts() # Retrieve posts from memcache
        # Datastore method to retrieve posts:
        # Post.all().order('-created')
        # GQL method to retrieve posts:
        # posts = db.GqlQuery('select * from Post order by created desc limit 10')
        if self.format == 'html':
            self.render('front.html', posts = posts)
        elif self.format == 'json':
            return self.render_json([p.as_dict() for p in posts])
