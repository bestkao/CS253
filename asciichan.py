import sys
import urllib2
from xml.dom import minidom
from handler import *
from art import *
import logging
import time

from google.appengine.api import memcache
from google.appengine.ext import db

'''
Add a map to the front page:
- Request IP -> Coordinates
    hostip.info
- Draw a map
    Google Maps (static map)
'''



art_key = db.Key.from_path('arts', 'default')

def console(s):
    sys.stderr.write('%s\n' %s)

IP_URL_BEG = 'http://api.hostip.info/?ip='
IP_URL_END = '&position=true'
# Makes a request to hostip.info using a given ip address
def get_coords(ip):
    # ip = '4.2.2.2'
    # ip = '23.24.209.141'
    url = IP_URL_BEG + ip + IP_URL_END # Sets the url using the given ip address
    content = None
    try:
        content = urllib2.urlopen(url).read() # Load and read url
    except URLError: # if the site is down
        return

    # Takes in an xml string and returns a GeoPt of (lat, lon)
    # if there are coordinates in the xml.
    if content:
        # parse the xml and find the coordinates
        d = minidom.parseString(content)
        coords = d.getElementsByTagName('gml:coordinates')
        if coords and coords[0].childNodes[0].nodeValue:
            lon, lat = coords[0].childNodes[0].nodeValue.split(',')
            return db.GeoPt(lat, lon)

# Returns the google maps image
# for a map with the GeoPts passed in.
GMAPS_URL = 'http://maps.googleapis.com/maps/api/staticmap?size=380x263&sensor=false&'
def gmaps_img(points):
    markers = '&'.join('markers=%s,%s' % (p.lat, p.lon)
                       for p in points)
    return GMAPS_URL + markers

def top_arts(update = False):
    key = 'top'
    arts = memcache.get(key)
    if not arts or update:
        logging.error("DB QUERY")

        # GQL query for a list of 10 most recent ascii art entities
        arts = db.GqlQuery('SELECT * '
                           'FROM Art '
#                           'WHERE ANCESTOR IS :1 '
                           'ORDER BY created DESC '
                           'LIMIT 10')
#                           art_key)
        
        # Create a list on the cursor arts to
        # prevent the running of multiple queries
        arts = list(arts)
        memcache.set(key, arts)
    
    return arts

# This is a blog of ascii art

class AsciiChan(Handler):
    # Render the 10 most recent ascii art posts
    def render_ascii(self, title = '', art = '', error = ''):
        arts = top_arts()

        # Find which arts have coordinates
        points = filter(None, (a.coords for a in arts))
        # Method 2:
        # points = []
        # for a in arts:
        #     if arts.coords:
        #         points.append(a.coords)

        # Confirm by writing out the coordinates
        # self.write(repr(points))

        # If we have any arts coords, make an image url
        img_url = None
        if points:
            img_url = gmaps_img(points)

        # Display the image url
        self.render('asciichan.html', title = title, art = art,
                    error = error, arts = arts, img_url = img_url)

    def get(self):
        # Confirm our IP address
        #   remote_addr is the requesting ip address
        # self.write(self.request.remote_addr)
        
        # Confirm get_coords() retrieves our coordinates
        #   repr() encloses its parameter with quotes
        # self.write(repr(get_coords(self.request.remote_addr)))
        return self.render_ascii()

    def post(self):
        title = self.request.get('title')
        art = self.request.get('art')
        
        if title and art:
            # Make a new instance of Art
            a = Art(parent = art_key, title = title, art = art)
            # lookup the user's coordinates from their IP
            coords = get_coords(self.request.remote_addr)
            # if we have coordinates, add them to Art
            if coords:
                a.coords = coords

            # stores the new instance into the database
            a.put()
            # rerun the query and update the cache
            top_arts(True)
            time.sleep(1)
            
            self.redirect('/asciichan')
        else:
            error = 'We need both a title and some artwork!'
            self.render_ascii(title, art, error)
