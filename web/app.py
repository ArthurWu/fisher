import web, os, sys
import json
import ConfigParser

ROOT = os.path.dirname(__file__)
TEMPLATES_DIR = os.path.join(ROOT, 'templates')
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(PROJECT_DIR)

import fit

urls = (
	'/', 'Index', 
	'/test-results', 'TestResult'
)

render = web.template.render(TEMPLATES_DIR)

class Index:
	def GET(self):
		return render.index()

class TestResult:
	CACHE_RESULTS = None

	def GET(self):
		if self.CACHE_RESULTS:
			return json.dumps(self.CACHE_RESULTS)
		else:
			results = fit.check_results()
			self.CACHE_RESULTS = results
			return json.dumps(results)

if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()