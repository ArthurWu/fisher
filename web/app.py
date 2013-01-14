import os, sys
ROOT = os.path.dirname(__file__)
TEMPLATES_DIR = os.path.abspath(os.path.join(ROOT, 'templates'))
PUBLIC_DIR = os.path.abspath(os.path.join(ROOT, 'public'))
PROJECT_DIR = os.path.abspath(os.path.join(ROOT, '..'))
PACKAGES_DIR = os.path.abspath(os.path.join(ROOT, '../packages'))
sys.path.extend([PROJECT_DIR, PACKAGES_DIR])

import web
import json

urls = (
	'/', 'Index', 
	'/public/(.*)', 'Public',
	'/test-results', 'views.testresult.TestResult'
)

render = web.template.render(TEMPLATES_DIR)

class Index:
	def GET(self):
		return render.index()

class Public:
	def GET(self, file):
		try:
			f = open(os.path.join(PUBLIC_DIR, file), 'r')
			return f.read()
		except:
			return web.webapi.NotFound()

application = web.application(urls, globals()).wsgifunc()
if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()