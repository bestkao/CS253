import webapp2
import cgi

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

form="""
<!DOCTYPE html>
<html>
    <head>
        <title>ROT 13 Encryption by James Kao</title>
    </head>
    <body>
        <h2>Enter some text to ROT13:</h2>
        <form method="post">
            <textarea name="text" style="height: 100px; width: 400px">%(text)s</textarea>
            <br>
            <input type="submit">
        </form>
    </body>
</html>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Hello, Udacity!")

class Rot13Handler(webapp2.RequestHandler):
    def escape_html(self, text=""):
        return cgi.escape(text, quote = True)

    def rot13(self, text=""):
        return text.encode('rot13')

    def write_form(self, text=""):
        self.response.write(form % {"text": text})

    def get(self):
        self.write_form()

    def post(self):
        user_text = str(self.request.get("text"))
        encrypted_text = self.rot13(user_text)
        escaped_text = self.escape_html(encrypted_text)
        self.write_form(escaped_text)

application = webapp2.WSGIApplication([("/", MainPage),
                                        ("/unit2/rot13", Rot13Handler)],
                                        debug=True)
