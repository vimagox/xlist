import argparse
import requests
from lxml import html


SCREEN_OUTPUT = 'screen'
HTML_OUTPUT = 'html'


CRAIGSLIST_CITY_URL = 'http://{}.craigslist.org/{}'


def find(categories, keywords, cities, output):
	"""
	Finds craigslist data in different cities
	:param categories: List of craigslist categories (ie: sof for Software jobs)
	:param keywords: List of keywords to look for
	:para cities: List of cities to look into
	:param output: Desired output format (options: screen/html)
	"""
	for cat in categories:
		for city in cities:
			print "---------------------------------------------------------------------"
			city_url = CRAIGSLIST_CITY_URL.format(city, cat)
			print '>>Looking in {}'.format(city_url)
			r = requests.get(city_url)
			if r.status_code == 200:
				tree = html.fromstring(r.text)
				jobs = tree.xpath('//p[@class="row"]/span[@class="pl"]/a/text()')
				for job in jobs:
		 			for keyword in keywords:
		 				if  keyword.upper() in job.upper():
		 					try:
		 						if output == SCREEN_OUTPUT:
		 							print '----{} : {}'.format(keyword, job)
		 						break
		 					except Exception:
		 						#UnicodeEncodeError: 'ascii' codec can't encode character u'\u200b' in position 0: ordinal not in range(128)
		 						print 'ERROR: Unable to display a job in {}'.format(city)
			else:
				print 'ERROR: Unable to find city: {}'.format(city)

