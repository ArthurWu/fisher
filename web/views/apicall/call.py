import web
import models
from request import Request

class Call:
	def GET(self):
		url, user, pwd = self.get_params()
		models.url.add_url_if_not_exist(url, user, pwd)
		return Request(url, user, pwd).GET().read()
		
	def PUT(self):
		url, user, pwd = self.get_params()
		models.url.add_url_if_not_exist(url, user, pwd)
		return Request(url, user, pwd).PUT().read()
	
	def get_params(self):
		url = web.input().url
		user = web.input(user=r'warrior\administrator').user
		pwd = web.input(pwd=r'1').password
		
		return url, user, pwd