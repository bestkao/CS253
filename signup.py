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
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        params = dict(username = username,
                      email = email)

        if not valid_username(username):
            params['error_username'] = "That's not a valid username."
            have_error = True

        if not valid_password(password):
            params['error_password'] = "That wasn't a valid password."
            have_error = True
        elif password != verify:
            params['error_verify'] = "Your passwords didn't match."
            have_error = True

        if not valid_email(email):
            params['error_email'] = "That's not a valid email."
            have_error = True

        # if user already exists:
            # params['error_username'] = 'That user already exists.'
            # have_error = True

        if have_error: # or invalid cookie
            self.render('signup-form.html', **params)
        else:
            # set cookie using valid username and password
            # with a user_id = 'value'|'hash'
            self.redirect('/unit3/welcome') # which renders 'Welcome, {{username}}!'
            # self.redirect('/welcome?username=' + username)

    def check_cookie(self, username):
        pass

####################################################################################

