import web
import models
from request import Request

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
		res = models.url.del_url(url)
		return res > 0 
			
	def _do(self, method):
		url = web.input(url='').url
		url_obj = models.url.get_url(url)
		if url_obj:
			return getattr(Request(url_obj.url, url_obj.user, url_obj.password), method)().read()
			
	def _get_actual_on(self):
		url = web.input(url='').url
		url_obj = models.url.get_url(url)
		url_obj.url = url_obj.url.replace('?', '/actual_on?')
		if url_obj: 
			return Request(url_obj.url, url_obj.user, url_obj.password).GET().read();
	