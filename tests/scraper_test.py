import unittest
import requests
from lxml import html


CITIES = ['boston', 'elpaso', 'lascruces', 'albuquerque', 'santafe', 'austin',
          'sanantonio', 'dallas', 'tucson', 'atlanta', 'lasvegas', 'chicago',
          'denver', 'detroit', 'houston', 'losangeles', 'miami', 'minneapolis',
          'newyork', 'orangecounty', 'palmsprings', 'prescott', 'reno', 'sacramento',
          'sandiego', 'sanluisobispo', 'seattle', 'sfbay', 'washingtondc']

KEYWORDS = ['java']


scraper = CraigslistScraper(CITIES, KEYWORDS)

class CraigslistScraperTest(unittest.TestCase):

	def test_cities_exist():
		scrape
		
