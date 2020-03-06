from textblob import TextBlob
import requests
from bs4 import BeautifulSoup

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
headers = {"user-agent": USER_AGENT}

class Analysis:
	def __init__(self,term):
		self.term = term
		self.subjectivity = 0
		self.sentiment = 0
		self.parseList = []

		self.search = self.term.replace(' ', '+')
		self.url = f"https://google.com/search?q={self.search}"

	def run(self):
		response = requests.get(self.url, headers=headers)

		if response.status_code == 200:
		    soup = BeautifulSoup(response.content, "html.parser")
		    retlst = []
		    for res in soup.find_all('div', class_='r'):
		        anchors = res.find_all('a')
		        if anchors:
		            link = anchors[0]['href']
		            title = res.find('h3').text
		            item = (("title",title),("link",link))
		            self.parseList.append(item)
		return(self.parseList)

	def titles(self):
		# print(self.run(),"1")
		retlst = []
		for i in self.parseList:
			 retlst.append(self.parseList[0][0][1])
		return retlst

	def links(self):
		# print(self.run(),"1")
		retlst = []
		for i in self.parseList:
			 retlst.append(self.parseList[0][1][1])
		return retlst

	def getLinkFromTitle(self,title_index):
		for i in self.parseList:
			return self.parseList[title_index][1][1]

def prompt_User():
	search = input("What search term would you like to load?\n")
	# Print Options
	while True:
		what = input("What would you like to do?\n")
		if (what=="1"):
			print(search.run())
		elif (what=="2"):
			print(search.titles())
		elif (what=="3"):
			print(search.links())
		elif (what=="f"):
			index = input("What index is the link that you would like to get?\n")
			print(search.getLinkFromTitle(index))
		else:
			break 

def main():
	#search = input("What is your search term?: ")
	search = "Black Business New York"
	entry = Analysis(search)
	entry.run()
	print(entry.links())
	print(entry.getLinkFromTitle(0))
main()
