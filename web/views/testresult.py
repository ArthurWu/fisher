import web
import json
from testcontroller import fit
import utils

class TestResult:
	def GET(self):
		params = web.input(reflash='true')
		res = {'actual_on': None, 'tests': []}
		
		if params.reflash == 'true':
			results = fit.check_results(team=params.team)
			utils.write_cache(results)
			res['tests'] = results
		elif params.reflash == 'false' and utils.has_cache():
			res['tests'] = json.loads(utils.read_cache())

		actual_on = utils.cache_time()
		res['actual_on'] = actual_on
		return json.dumps(res)