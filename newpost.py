from handler import *
from post import *

# A form to submit new posts

class NewPost(Handler):
    def get(self):
        self.render('newpost.html')

    def post(self):
        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            p = Post(parent = blog_key(), subject = subject, content = content)
            p.put()
            self.redirect('/blog/%d' % p.key().id())
        else:
            error = 'subject and content, please!'
            self.render('newpost.html', subject = subject, content = content, error = error)
