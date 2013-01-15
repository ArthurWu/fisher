from settings import render

class Index:
	def GET(self):
		return render.apicall.index()