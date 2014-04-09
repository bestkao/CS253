from handler import Handler

# A handler to logout a user

class Logout(Handler):
    def get(self):
        self.logout()
        self.redirect('/blog')