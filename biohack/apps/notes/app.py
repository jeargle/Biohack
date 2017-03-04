# Notes Web API

import os.path
from tornado import web

# Absolute paths
app_path = os.path.split(os.path.abspath(__file__))[0]
pkg_path = os.path.split(app_path)[0]
biohack_path = os.path.split(pkg_path)[0]

# Computed paths
global_static = os.path.join(biohack_path,  os.path.join('lib', 'www', 'static'))
local_static  = os.path.join(app_path, 'static')

local_templates  = os.path.join(app_path, 'templates')
global_templates  = os.path.join(pkg_path, 'main', 'templates')

local_html  = os.path.join(app_path, 'static', 'html')
global_html  = os.path.join(pkg_path, 'main', 'static', 'html')


class NotesHandler(web.RequestHandler):
    def get(self, filename = None):
        if filename is None:
            self.render(os.path.join(local_html, 'index.html'))
        else:
            self.render(os.path.join(local_html, '%s.html' % (filename)))
        return



urls = [
    (r'/notes', NotesHandler),
    (r'/notes/static/(.*)', web.StaticFileHandler, {'path': local_static}),
    (r'/notes/(.*)', NotesHandler),
]
