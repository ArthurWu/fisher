import web
import settings

urls = (
	'/', 'views.index.Index',
	'/test-results', 'views.testresult.TestResult',
	'/tools/api-call', 'views.apicall.index.Index',
	'/tools/call', 'views.apicall.call.Call'
)

#application = web.application(urls, globals()).wsgifunc()
if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()