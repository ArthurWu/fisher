import web
from datetime import datetime
import os
DB_PATH = os.path.join(os.path.dirname(__file__), '../database/data.sqlite')

db = web.database(dbn='sqlite', db=DB_PATH)

def get_urls():
	return db.select('url', order='created')
	
def get_url(url):
	try:
		return db.select('url', where='url=$url', vars=locals())[0]
	except IndexError:
		return None;

def add_url_if_not_exist(url, user, password):
	exist = db.select('url', locals(), where='url=$url and user=$user and password=$password')
	if not exist: db.insert('url', url=url, user=user, password=password, created=datetime.now())
	
def del_url(url):
	return db.delete('url', where='url=$url', vars=locals())