from __future__ import unicode_literals
import multiprocessing
import gunicorn.app.base
from gunicorn.six import iteritems
from ladon.server.wsgi import LadonWSGIApplication
from os.path import abspath, dirname
 
# The ladon wsgi application
application = LadonWSGIApplication(
              ['calculator'],
              [dirname(abspath(__file__))],
              catalog_name='My Ladon webservice catalog',
              catalog_desc='This is the root of my cool webservice catalog')
 
# Inherit from gunicorn base application class to create our application
class StandaloneApplication(gunicorn.app.base.BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(StandaloneApplication, self).__init__()
 
    # Extract config options
    def load_config(self):
        config = dict([(key, value) for key, value in iteritems(self.options)
                 if key in self.cfg.settings and value is not None])
 
        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)
 
    def load(self):
        return self.application
 
 
if __name__ == '__main__':
# Set the options
    options = {
        # For simplicity I am using these default configurations: 
        # Localhost Ip(127.0.0.1), Default Port(5656) and Default no. of workers 4
        # You can take arguments from the command line for these attributes
        'bind': '%s:%s' % ('127.0.0.1', '5656'),
        'workers': 4,
    }
 
# Run the application
StandaloneApplication(application, options).run()
