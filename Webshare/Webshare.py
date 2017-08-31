import requests
import random
import datetime
import threading
import uuid
import time

class Webshare():
	"""
		Wrapper for Webshare Proxy API with randomization and threading.
	"""
	def __init__(self, username, password):
		__author__		= "Sergio Molanes"
		__creation__		= "08/29/2017"
		__email__		= "sergio@hlx.co"
		__site__		= "http://hlx.co"
		self.PROXYSTRING = "http://{0}-{2}:{1}@proxyserver.webshare.io:3128/"
		self.Username = username
		self.Password = password
		self.URL_LIST = []
		self.THREADS = []
		self.RESULT_LIST = []

	def getURL(self, url, randomProxy = True):
		"""
			Retrieves a URL through a proxy.
			The proxy is randomized between requests if randomProxy is true.
			Results are appended to the collection for use with threading.
		"""
		if randomProxy == True:
			proxyValue = random.randint(1,100)
		else:
			proxyValue = 1
		proxyDict = {"https": self.PROXYSTRING.format(self.Username
							, self.Password
							, proxyValue)}
		# - The resulting data is appended to the set in the event that 
		# -	this is being used while threading.  Otherwise, it can be ignored.
		result = requests.get(url, proxies = proxyDict)
		result_dict = {"Datetime":datetime.datetime.now()
				,"Hyperlink":url
				,"Status":result.status_code
				,"Text":result.text
				,"UUID":uuid.uuid4()}
		self.RESULT_LIST.append(result_dict)
		return result

	def thread_getURL(self, urlList, threadCount = 2, sleepTime = 0.5):
		self.URL_LIST = urlList
		while len(self.URL_LIST) > 0:
			# - - - Remove dead threads before beginning
			for th in self.THREADS:
				if not th.isAlive():
					self.THREADS.remove(th)
			if len(self.THREADS) >= threadCount:
				time.sleep(sleepTime)
				continue
			print("adding")
			current_URL = self.URL_LIST.pop()
			t = threading.Thread(name = "getURL\t{}".format(current_URL)
				, target= self.getURL
				, kwargs={'url':current_URL, 'randomProxy':True})
			self.THREADS.append(t)
			t.start()
		t.join()
