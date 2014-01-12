import webapp2
from escape_html import escape_html
from signupValidation import *

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

signup_form="""
<!DOCTYPE html>

<html>
  <head>
    <title>Sign Up</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
    <h2>Signup</h2>
    <form method="post">
      <table>
        <tr>
          <td class="label">
            Username
          </td>
          <td>
            <input type="text" name="username" value=%(username)s>
          </td>
          <td class="error">
            %(username_error)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Password
          </td>
          <td>
            <input type="password" name="password" value="">
          </td>
          <td class="error">
            %(password_error)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Verify Password
          </td>
          <td>
            <input type="password" name="verify" value="">
          </td>
          <td class="error">
            %(verify_error)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Email (optional)
          </td>
          <td>
            <input type="text" name="email" value=%(email)s>
          </td>
          <td class="error">
            %(email_error)s
          </td>
        </tr>
      </table>

      <input type="submit">
    </form>
  </body>

</html>
"""

welcome_form="""
<!DOCTYPE html>
<html>
  <head>
    <title>Unit 2 Signup</title>
  </head>
  <body>
    <h2>Welcome, %s!</h2>
  </body>
</html>
"""

class Signup(webapp2.RequestHandler):
    def write_form(self, username="", email="", username_error="",
                   password_error="", verify_error="", email_error=""):
        self.response.out.write(signup_form % {"username": escape_html(username),
                                               "email": escape_html(email),
                                               "username_error": escape_html(username_error),
                                               "password_error": escape_html(password_error),
                                               "verify_error": escape_html(verify_error),
                                               "email_error": escape_html(email_error)})

    def get(self):
        self.write_form()

    def post(self):
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        username_error = ""
        password_error = ""
        verify_error = ""
        email_error = ""

        if not valid_username(username):
            username_error = "That's not a valid username."
            have_error = True

        if not valid_password(password):
            password_error = "That wasn't a valid password."
            have_error = True
        elif password != verify:
            verify_error = "Your passwords didn't match."
            have_error = True

        if not valid_email(email):
            email_error = "That's not a valid email."
            have_error = True

        if have_error:
            self.write_form(username, email, username_error,
                             password_error, verify_error, email_error)
        else:
            self.redirect('/unit2/welcome?username=%s' % username)

class Welcome(webapp2.RequestHandler):
    def get(self):
        username = self.request.get("username")
        if valid_username(username):
            self.response.out.write(welcome_form % username)
        else:
            self.redirect("/unit2/signup")