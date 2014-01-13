import os
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

# A basic web app that says "Hello, Udacity!"

class Main(webapp2.RequestHandler):
    def get(self):
    	t_values = {
    		"text": "Hello, Udacity!"
    	}
    	t = jinja_env.get_template('index.html')
        self.response.write(t.render(t_values))
