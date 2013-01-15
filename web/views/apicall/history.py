from settings import render
import models

class History:
	def GET(self):
		data = models.url.get_urls()
		return render.apicall.history(data)