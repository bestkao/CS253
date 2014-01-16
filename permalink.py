from handler import *
from post import Post

## This is a permalink page for posts

class Permalink(Handler):
    def get(self, post_id):
        p = Post.get_by_id(int(post_id))
        self.render("blog.html", posts = [p])
