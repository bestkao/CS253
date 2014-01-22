from handler import *
import hmac

SECRET = 'iamsosecret'

# HMAC hashing using a secret key
def hash_str(s):
	return hmac.new(SECRET, s).hexdigest()

# Takes a string and returns a string of the format: 
# s|HASH
def make_secure_val(s):
	return "%s|%s" % (s, hash_str(s))

# Takes a string of the format: h|HASH
# and returns h if hash_str(h) == HASH, otherwise None 
def check_secure_val(h):
	val = h.split("|")[0]
	if h == make_secure_val(val):
		return val

class Cookie(Handler):
	def get(self):
		self.response.headers["Content-Type"] = "text/plain"
		visits = 0
		# Retrieve the value of the key 'visits' if it exists, defaults to None
		visit_cookie_str = self.request.cookies.get("visits")
		if visit_cookie_str:
			cookie_val = check_secure_val(visit_cookie_str)
			if cookie_val:
				visits = int(cookie_val) # since cookie_val is a string

        # Update the new cookie value
		visits += 1
		new_cookie_val = make_secure_val(str(visits))

        # Set the cookie header to 'visits=new_cookie_val'
		self.response.headers.add_header("Set-Cookie", "visits=%s" % new_cookie_val)

		if visits > 10000:
			self.write("You are the best ever!")
		else:
			self.write("You've been here %s times!" % visits)