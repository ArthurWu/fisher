from settings import *

urls = (
	'/', 'views.index.Index',
	'/test-results', 'views.testresult.TestResult',
	'/tools/api-call', 'views.apicall.index.Index',
	'/tools/call', 'views.apicall.call.Call'
	'/public/(.*)', 'Public',
)

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

#application = web.application(urls, globals()).wsgifunc()
if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()