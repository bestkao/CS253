from handler import *
from date import *

# This is a web app that checks for a valid birthday and redirects to a thanks page if valid.

class Birthday(Handler):

    def render_birthday(self, error = "", month = "", day = "", year = ""):
        self.render("birthday.html", error = error, month = month, day = day, year = year)

    def get(self):
        self.render_birthday()

    def post(self):
        user_month = self.request.get("month")
        user_day = self.request.get("day")
        user_year = self.request.get("year")

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if not (month and day and year):
            self.render_birthday("That doesn't look valid to me, friend.",
                            user_month, user_day, user_year)
        else:
            self.redirect("/thanks")

