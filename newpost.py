from handler import *
from post import *

# A form to submit new posts

class NewPost(Handler):
    def get(self):
        if self.user:
            self.render('newpost.html')
        else:
            self.redirect('/login')

    def post(self):
        if not self.user:
            self.redirect('/blog')

        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            p = Post(parent = blog_key(), subject = subject, content = content)
            p.put()
            
            # rerun the query and update the cache
            top_posts(True)
            time.sleep(1)

            self.redirect('/blog/%d' % p.key().id())
        else:
            error = 'subject and content, please!'
            self.render('newpost.html', subject = subject, content = content, error = error)
