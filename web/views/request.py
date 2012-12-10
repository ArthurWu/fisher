import urllib2
from ntlm import HTTPNtlmAuthHandler
from urlparse import urlsplit

class Request:
	def __init__(self, url, user, pwd):
		self.url = url
		self.user = user
		self.password = pwd
		
	def GET(self):
		passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
		passman.add_password(None, self.url, self.user, self.password)
		# create the NTLM authentication handler
		auth_NTLM = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(passman)

		# create and install the opener
		opener = urllib2.build_opener(auth_NTLM)
		urllib2.install_opener(opener)

		# retrieve the result
		response = urllib2.urlopen(self.url)
		return response
		
	def PUT(self):	
		passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
		passman.add_password(None, self.url, self.user, self.password)
		# create the NTLM authentication handler
		auth_NTLM = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(passman)

		# create and install the opener
		opener = urllib2.build_opener(auth_NTLM)
		req = urllib2.Request(self.url, urlsplit(self.url).query)
		req.add_header('Content-Type', 'text/json')
		req.get_method = lambda: 'PUT'
		
		res = opener.open(req)		
		return res
		
	def POST(self):
		passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
		passman.add_password(None, self.url, self.user, self.password)
		# create the NTLM authentication handler
		auth_NTLM = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(passman)

		# create and install the opener
		opener = urllib2.build_opener(auth_NTLM)
		req = urllib2.Request(self.url, urlsplit(self.url).query)
		req.add_header('Content-Type', 'text/json')
		req.get_method = lambda: 'POST'
		
		res = opener.open(req)		
		return res	
		
if __name__ == '__main__':
	url = r'http://arthur10:3141/api/security/counters/open_content?url=http://arthur10/sites/sc3'
	actual_on_url = r'http://arthur10:3141/api/security/counters/open_content/actual_on?url=http://arthur10/sites/sc3'
	user = r'warrior\administrator'
	password = '1'
	method = 'PUT'
	
	print Request(url, user, password, method).PUT().read()
	print Request(url, user, password, method).GET().read()
	print Request(actual_on_url, user, password, method).GET().read()
	
		
	