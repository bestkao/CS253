import webapp2
<<<<<<< HEAD
import cgi
from signupValidation import *

'''
Instructor Notes:
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

rot13_form="""
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
            <input type="password" name="password">
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
            <input type="password" name="verify">
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

def escape_html(text=""):
        return cgi.escape(text, quote = True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Hello, Udacity!")

class Rot13Handler(webapp2.RequestHandler):
    def rot13(self, text=""):
        return text.encode('rot13')

    def write_form(self, text=""):
        self.response.write(rot13_form % {"text": text})

    def get(self):
        self.write_form()

    def post(self):
        user_text = str(self.request.get("text"))
        encrypted_text = self.rot13(user_text)
        self.write_form(escape_html(encrypted_text))

class SignupHandler(webapp2.RequestHandler):
    def write_form(self, username_error="", password_error="", verify_error="",
                email_error="", username="", password="", verify="", email=""):
        self.response.write(signup_form % {"username_error": username_error,
                                    "password_error": password_error,
                                    "verify_error": verify_error,
                                    "email_error": email_error,
                                    "username": escape_html(username),
                                    "password": escape_html(password),
                                    "verify": escape_html(verify),
                                    "email": escape_html(email)})
=======
from dateValidation import *

form="""
<form method="post">
    What is your birthday?
    <br>
    <label>Month 
        <input type="text" name="month" value=%(month)s>
    </label>
    <label>Day 
        <input type="text" name="day" value=%(year)s>
    </label>
    <label>Year 
        <input type="text" name="year" value=%(year)s>
    </label>
    <div style="color: red">%(error)s</div>
    <br>
    <br>
    <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.write(form % {"error": error,
                                    "month": escape_html(month),
                                    "day": escape_html(day),
                                    "year": escape_html(year)})
>>>>>>> 1d8cc4998f8258f132b3891cfa93c62f5ff07af7

    def get(self):
        self.write_form()

    def post(self):
<<<<<<< HEAD
        """
        user_username = self.request.get("username")
        user_password = self.request.get("password")
        user_verify = self.request.get("verify")
        user_email = self.request.get("email")

        username = valid_username(user_username)
        password = valid_password(user_password)
        verify = valid_verify(user_verify)
        email = valid_email(user_email)

        #if not (username and password and verify and email):
        #    self.write_form("That doesn't look valid to me, friend.",
                            username, password, verify, email)
        #else:
        """
        self.redirect("/unit2/welcome")

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get("username")
        self.response.out.write(username)

application = webapp2.WSGIApplication([("/", MainPage),
                                       ("/unit2/rot13", Rot13Handler),
                                       ("/unit2/signup", SignupHandler),
                                       ("/unit2/welcome", WelcomeHandler)],
                                       debug=True)
=======
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if not (month and day and year):
            self.write_form("That doesn't look valid to me, friend.",
                            user_month, user_day, user_year)
        else:
            self.redirect("/thanks")

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Thanks! That's a totally valid date!")

application = webapp2.WSGIApplication([('/', MainPage),
                                      ('/thanks', ThanksHandler)],
                                      debug=True)
>>>>>>> 1d8cc4998f8258f132b3891cfa93c62f5ff07af7
