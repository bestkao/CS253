import webapp2

"""
Homework 1
  - Install Google App Engine
  - Put online a basic app that says "Hello, Udacity!"
  - Submit the URL
"""

class Main(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Hello, Udacity!")
