"""
requests cache
"""
import os
import re
import requests
import datetime
from settings import CACHE_DIRECTORY


def _cached_items(url, city, cat, cache_directory):
	directory = '{}/{}'.format(cache_directory, datetime.date.today())
	if not os.path.exists(directory):
		os.makedirs(directory)	
	file_name = '{}-{}.html'.format(city, cat)
	file_path = '{}/{}'.format(directory, file_name).lower()
	text = None
	if os.path.exists(file_path):
		text = open(file_path, 'r').read()
	else:
		r = requests.get(url)
		if r.status_code == 200:
			text = r.text
			_file = open(file_path, 'w')
			_file.write(text)
			_file.close()
	return text


def _cached_cities(url, region, cache_directory):
	file_path = '{}/{}_cities.html'.format(cache_directory, region).lower()
	if os.path.exists(file_path):
		text = open(file_path, 'r').read()
	else:
		r = requests.get(url)
		if r.status_code == 200:
			text = r.text
			_file = open(file_path, 'w')
			_file.write(text)
			_file.close()
	return text


def get(url, cache_directory=CACHE_DIRECTORY):
	match = re.search(r"http://www.craigslist.org/about/sites#(\S*)", url)
	if match:
		return _cached_cities(url, match.groups()[0], cache_directory)
	match = re.search(r"http://(\S*).craigslist.org/(\S*)", url)
	if match:
		city, cat = match.groups()[0], match.groups()[1]
		return _cached_items(url, city, cat, cache_directory)
	return None
