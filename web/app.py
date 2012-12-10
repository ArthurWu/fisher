import os, sys
ROOT = os.path.dirname(__file__)
TEMPLATES_DIR = os.path.abspath(os.path.join(ROOT, 'templates'))
PROJECT_DIR = os.path.abspath(os.path.join(ROOT, '..'))
PACKAGES_DIR = os.path.abspath(os.path.join(ROOT, '../packages'))
sys.path.extend([PROJECT_DIR, PACKAGES_DIR])

import web
import json

urls = (
	'/', 'Index', 
	'/test-results', 'views.testresult.TestResult'
)

render = web.template.render(TEMPLATES_DIR)

class Index:
	def GET(self):
		return render.index()

application = web.application(urls, globals()).wsgifunc()
if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()