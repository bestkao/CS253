import os
import jinja2
import webapp2
import cgi
from date import *

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = False)

"""
This is a web app that checks for a valid birthday and redirects to a thanks page if valid.
"""

class Birthday(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        t_values = {
            "error": error,
            "month": cgi.escape(month, quote = True),
            "day": cgi.escape(day, quote = True),
            "year": cgi.escape(year, quote = True)
        }
        t = jinja_env.get_template('birthday.html')
        self.response.write(t.render(t_values))

    def get(self):
        self.write_form()

    def post(self):
        user_month = self.request.get("month")
        user_day = self.request.get("day")
        user_year = self.request.get("year")

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if not (month and day and year):
            self.write_form("That doesn't look valid to me, friend.",
                            user_month, user_day, user_year)
        else:
            self.redirect("/unit2/thanks")

class Thanks(webapp2.RequestHandler):
    def get(self):
        self.response.write("Thanks! That's a totally valid date!")
