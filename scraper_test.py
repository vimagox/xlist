import unittest
import requests
from lxml import html


CITIES = ['boston', 'elpaso', 'lascruces', 'albuquerque', 'santafe', 'austin',
          'sanantonio', 'dallas', 'tucson', 'atlanta', 'lasvegas', 'chicago',
          'denver', 'detroit', 'houston', 'losangeles', 'miami', 'minneapolis',
          'newyork', 'orangecounty', 'palmsprings', 'prescott', 'reno', 'sacramento',
          'sandiego', 'sanluisobispo', 'seattle', 'sfbay', 'washingtondc']

KEYWORDS = ['java']


CRAIGSLIST_URL = 'http://{}.craigslist.org/sof'

def scrape(url):
	r = requests.get(url)
	return r.status_code, r.text

# reading lines like any other language
def read_lines2(text):
	lines = []
	for line in text.split('\n'):
		lines.append(line)
	return lines

# reading lines the python way (list comprehensions)
def read_lines(text):
	return [line for line in text.split('\n')]

def test_scraper():
	for city in CITIES:
		print "---------------------------------------------------------------------"
		print 'Looking in {}'.format(city)
		status, text = scrape(CRAIGSLIST_URL.format(city))
		assert(status == 200)
		tree = html.fromstring(text)
		jobs = tree.xpath('//p[@class="row"]/span[@class="pl"]/a/text()')
		for job in jobs:
		 	for keyword in KEYWORDS:
		 		if  keyword.upper() in job.upper():
		 			print '>>>{} : {}'.format(keyword, job)
		 			break
		
