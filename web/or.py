import web
from request import Request
import model
import os

ROOT = os.path.dirname(__file__)
TEMPLATES_DIR = os.path.join(ROOT, 'templates')

urls = (
	'/', 'Index',
	'/open', 'Openurl',
	'/history', 'History',
	'/action', 'Action'
)

render = web.template.render(TEMPLATES_DIR, base='base')

class Index:
	def GET(self):
		return render.index()
		
class Openurl:
	def GET(self):
		url, user, pwd = self.get_params()
		model.add_url_if_not_exist(url, user, pwd)
		return Request(url, user, pwd).GET().read()
		
	def PUT(self):
		url, user, pwd = self.get_params()
		model.add_url_if_not_exist(url, user, pwd)
		return Request(url, user, pwd).PUT().read()
	
	def get_params(self):
		host = web.input().host
		url = web.input().url
		user = web.input(user=r'warrior\administrator').user
		pwd = web.input(pwd=r'1').password
		
		return host+url, user, pwd
	
class History:
	def GET(self):
		data = model.get_urls()
		return render.history(data)

class Action:
	def GET(self):
		type = web.input(type='').type
		if type == 'actual_on':
			return self._get_actual_on()
		elif type == 'delete':
			return self._delete()
		else:
			return self._do('GET')
	
	def PUT(self):
		return self._do('PUT')
		
	def _delete(self):
		url = web.input(url='').url
		res = model.del_url(url)
		return res > 0 
			
	def _do(self, method):
		url = web.input(url='').url
		url_obj = model.get_url(url)
		if url_obj:
			return getattr(Request(url_obj.url, url_obj.user, url_obj.password), method)().read()
			
	def _get_actual_on(self):
		url = web.input(url='').url
		url_obj = model.get_url(url)
		url_obj.url = url_obj.url.replace('?', '/actual_on?')
		if url_obj: 
			return Request(url_obj.url, url_obj.user, url_obj.password).GET().read();
	
application = web.application(urls, globals()).wsgifunc()

if __name__ == '__main__':
	app.run()