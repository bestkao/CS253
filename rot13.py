import os
import jinja2
import webapp2
import cgi

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = False)

"""
In order to be graded correctly for this homework, there are a
few things to keep in mind. We'll be grading your web app by
POSTing to your form and retrieving the text that has been
encoded with ROT13. There are a few main issues you need to keep
in mind in order for this to work:
The textarea form element where the user inputs the text to
encode must be named 'text'. In other words, you must have
'textarea name="text"' for us to post to. The form method must
be POST, not GET. You must enter the full url into the supplied
textbox above, including the path. For example, our example app
is running at http://udacity-cs253.appspot.com/unit2/rot13, but

if we instead only entered http://udacity-cs253.appspot.com/
then the grading script would not work. Don't forget to escape
your output!
"""

class Rot13(webapp2.RequestHandler):
    def rot13(self, text=""):
        return text.encode('rot13')

    def write_form(self, text=""):
        t_values = {
            "text": cgi.escape(text)
        }
        t = jinja_env.get_template('rot13.html')
        self.response.write(t.render(t_values))

    def get(self):
        self.write_form()

    def post(self):
        user_text = str(self.request.get("text"))
        encrypted_text = self.rot13(user_text)
        self.write_form(encrypted_text)
