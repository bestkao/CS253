from handler import *
from post import *

# Flushes the memcache

class Flush(Handler):
    def get(self):
        last_queried = 0
        last_queried_permalink = 0
        memcache.flush_all()
        self.redirect('/blog')
