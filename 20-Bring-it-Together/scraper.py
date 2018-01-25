#First Scraper + Challenge 1! Saving Headlines to File.

import os
import urllib.request
from bs4 import BeautifulSoup

class Scraper:
	def __init__(self, site): #website to scrape as parameter
		self.site = site

	def scrape(self): #method to call to scrape from passed site
		#urlopen function makes a request to site and returns response object (r)
		r = urllib.request.urlopen(self.site) 
		html = r.read() #returns the html from the response object
		#now we need to parse the HTML
		parser = "html.parser"
		sp = BeautifulSoup(html, parser)
		#BeautifulSoup does all the hard work and parses the HTML.
		#Now add code that calls the method findall on BeautifulSoup object.

		for tag in sp.find_all("a"): #returns iterable containing tag objects
			url = tag.get("href") #get the value of the href instance variable
			if url is None:
				continue
			if "html" in url:
				with open("headlines.txt", "a") as hl:
					hl.write(url + "\n")
					print("\n" + url)


news = "https://news.google.com/"
Scraper(news).scrape()

