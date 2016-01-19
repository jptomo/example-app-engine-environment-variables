import os

import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(
            'FOO: %s<br>BAR: %s' %
            (os.environ.get('FOO'),
             os.environ.get('BAR')))


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
