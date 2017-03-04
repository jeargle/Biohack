# Main Web API

import os.path
import sys
sys.path.append('/home/ec2-user')
from tornado import web
from biohack.apps.notes.app import urls as notes_urls
from biohack.apps.code.app import urls as code_urls
from biohack.apps.essays.app import urls as essays_urls

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


class IndexHandler(web.RequestHandler):
    def get(self):
        self.render(os.path.join(global_html, 'index.html'))



urls = [
    (r'/', IndexHandler),
    (r'/static/(.*)', web.StaticFileHandler, {'path': global_static}),
    (r'/main/static/(.*)', web.StaticFileHandler, {'path': local_static}),
    # (r'/(.*)', IndexHandler),
]

urls.extend(notes_urls)
urls.extend(code_urls)
urls.extend(essays_urls)


if __name__=='__main__':
    import logging
    from tornado import ioloop

    logging.getLogger().setLevel(logging.DEBUG)

    app = web.Application(urls, template_path = pkg_path, debug = True)
    # app.listen(80)
    app.listen(8005)

    ioloop.IOLoop.instance().start()
