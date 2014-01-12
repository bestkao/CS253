import webapp2
from escape_html import escape_html
from date import *

"""
Lesson 2:
This is a web app that checks for a valid birthday and redirects to a thanks page if valid.
"""

birthday_form="""
<form method="post">
    What is your birthday?
    <br>
    <label>Month 
        <input type="text" name="month" value=%(month)s>
    </label>
    <label>Day 
        <input type="text" name="day" value=%(day)s>
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

class Birthday(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.write(birthday_form % {"error": error,
                                             "month": escape_html(month),
                                             "day": escape_html(day),
                                             "year": escape_html(year)})

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
