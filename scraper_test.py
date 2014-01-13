import unittest
import requests


def scrape(url):
	r = requests.get(url)
	return r.status_code, r.text

def read_lines(text):
	lines = []
	for line in text.split('\n'):
		lines.append(line)
	return lines

def test_scraper():
	status, text = scrape('http://elpaso.craigslist.org')
	assert(status == 200)
	lines = read_lines(text)
	for line in lines:
		print ">>>>>>>>>>>>>>>",line