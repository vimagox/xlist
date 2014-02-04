import unittest
import glob
import os
import shutil
import datetime
import httpretty

from xlist.requests_cache import get


SAMPLE_CITY_URL = 'http://boston.craigslist.org/sof'
CITIES_URL =  'http://www.craigslist.org/about/sites#US'
CACHE_DIRECTORY = './tests/cache'

BOSTON_HTML = 'tests/samples/boston.html'
CITIES_HTML = 'tests/samples/us.html'


def _clean_cache():
    if os.path.exists(CACHE_DIRECTORY):
        _clean_dir(CACHE_DIRECTORY)

def _clean_dir(directory):
    files = glob.glob('{}/*'.format(directory))
    for f in files:
        if os.path.isfile(f):
            os.unlink(f)
        else:
            shutil.rmtree(f)


class CacheTest(unittest.TestCase):
    def setUp(self):
        _clean_cache()
        httpretty.register_uri(httpretty.GET, 
                           SAMPLE_CITY_URL,
                           body=open(BOSTON_HTML, 'r').read(),
                           content_type="text/html")
        httpretty.register_uri(httpretty.GET, 
                           CITIES_URL,
                           body=open(CITIES_HTML, 'r').read(),
                           content_type="text/html")        

    def tearDown(self):
        _clean_cache()

    @httpretty.activate
    def test_get_items(self):
        directory = '{}/{}'.format(CACHE_DIRECTORY, datetime.date.today())
        assert(os.path.exists(directory) == False)
        text = get(SAMPLE_CITY_URL, cache_directory=CACHE_DIRECTORY)
        assert(text is not None)
        assert(os.path.exists(directory) == True)
        assert(os.path.exists('{}/boston-sof.html'.format(directory)) == True)

    @httpretty.activate
    def test_get_cities(self):
        cities_file = '{}/us_cities.html'.format(CACHE_DIRECTORY)
        assert(os.path.exists(cities_file) == False)
        text = get(CITIES_URL, cache_directory=CACHE_DIRECTORY)
        assert(text is not None)
        assert(os.path.exists(cities_file) == True)
