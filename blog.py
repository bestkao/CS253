from handler import *

'''
Build a blog
  - Front page that lists entries
  - Form to submit new entries
  - Permalink page for entries

Instructor Notes:
In order to be graded correctly for this homework, there are a few things to
keep in mind. We'll be grading your web app by POSTing new blog entries to your
form and checking that they appear on your blog's front page. There are a few
main issues you need to keep in mind in order for this to work:

We assume your form to create new blog entries is at a path of '/newpost' from
your blog's front page. That is, if your blog's front page is at
'www.myblog.com/blog', then the form is at 'www.myblog.com/blog/newpost'.
The form method must be POST, not GET. The form input boxes must have the names
'subject' and 'content' in order for the grading script to correctly post to them.
You must enter the full url into the supplied textbox above, including the
path to your blog's front page. For example, our example app is running at
http://cs253-homework-sean.appspot.com/blog, but if we instead only entered
http://udacity-cs253.appspot.com/ then the grading script would not work.
Don't forget to escape your output!
'''

'''
A couple helpful links for HW 3:
I realized while recording the solution to HW 3 a few things that I didn't cover
in the lecture that will be helpful to know. After submitting a blog post, I ask
you to redirect to a permalink for that post. The url format might look something
like this: /blog/1001, where 1001 is the id of the post you just submitted.
To get the id of an entity you just created: obj.key().id()

Find some examples of more complex URL handling here:
    http://webapp-improved.appspot.com/guide/routing.html

To look up an object by id, you can use the get_by_id() function document here:
    https://developers.google.com/appengine/docs/python/datastore/modelclass#Model_get_by_id

Hope this helps!
'''

class Post(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True, indexed = False)
    created = db.DateTimeProperty(auto_now_add = True)
    #last_modified = db.DateTimeProperty(auto_now = True)

class Blog(Handler):
    def render_blog(self, subject = "", content = "", created = ""):
        # Google Datastore Query:
        posts = Post.all().order("-created")
        # GQL Query:
        # posts = db.GqlQuery("SELECT * FROM Post "
        #                     "ORDER BY created DESC LIMIT 10")
        self.render("blog.html", subject = subject, content = content, created = created, posts = posts)

    def get(self):
        self.render_blog()

class Permalink(Blog):
    def get(self, post_id):
        p = Post.get_by_id(int(post_id))
        self.render("blog.html", posts = [p])
