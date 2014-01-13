import unittest
import requests


def scrape(url):
	r = requests.get(url)
	return r.status_code, r.text


def read_lines(text):
	for line in text.split('/n'):
		print 'simon:'+line

def test_scraper():
	status, text = scrape('http://elpaso.craigslist.org')
	assert(status == 200)
	read_lines(text)