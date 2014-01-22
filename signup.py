from handler import *
from signup_validation import *

'''
In order to be graded correctly for this homework, there are a few things to keep in mind.
We'll be grading your web app by posting to your form and then checking the HTTP Response
we receive. There are a few main issues you need to keep in mind in order for this to work:

  - The form elements where the user inputs their username, password, password
    again, and email address must be named "username", "password", "verify", and
    "email", respectively.
  - The form method must be POST, not GET.
  - Upon invalid user input, your web app should re-render the form for the user.
  - Upon valid user input, your web app should redirect to a welcome page for the user.
    - This page must include both "Welcome" and the user's username.
  - You must enter the full url into the supplied textbox above, including the path. For
    example, our example app is running at http://udacity-cs253.appspot.com/unit2/signup,
    but if we instead only entered http://udacity-cs253.appspot.com/ then the grading script
    would not work.

Regular Expressions:
A regular expressions is a handy tool for matching text to a pattern. The regular
expressions that we're using to validate you input are as follows:
    Username: "^[a-zA-Z0-9_-]{3,20}$" Password: "^.{3,20}$" Email: "^[\S]+@[\S]+\.[\S]+$"
Example code for validating a username is as follows:
    import re
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    def valid_username(username):
        return USER_RE.match(username)
More information on using regular expressions in Python can be found here:
    http://docs.python.org/library/re.html
'''

class Signup(Handler):
    def get(self):
        self.render('signup-form.html')

    def post(self):
        have_error = False
        # Retrieve data entered in the text fields
        self.username = self.request.get('username')
        self.password = self.request.get('password')
        self.verify = self.request.get('verify')
        self.email = self.request.get('email')
        
        # Dictionary of parameters to re-render if the signup was invalid
        params = dict(username = self.username,
                      email = self.email)

        # Check every field for valid data
        if not valid_username(self.username):
            params['error_username'] = "That's not a valid username."
            have_error = True

        if not valid_password(self.password):
            params['error_password'] = "That wasn't a valid password."
            have_error = True
        elif self.password != self.verify:
            params['error_verify'] = "Your passwords didn't match."
            have_error = True

        if not valid_email(self.email):
            params['error_email'] = "That's not a valid email."
            have_error = True

        if have_error:
            self.render('signup-form.html', **params)
        else:
            self.done()

    def done(self, *a, **kw):
        raise NotImplementedError
