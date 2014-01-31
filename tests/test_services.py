"""
services tests
"""
import httpretty
from xlist.services import find, cities
from xlist.settings import CITIES_URL


BOSTON_SAMPLE_HTML = 'tests/samples/boston.html'
US_SAMPLE_HTML = 'tests/samples/us.html'


def _setup_mock_responses():
    httpretty.register_uri(httpretty.GET, 
                           "http://boston.craigslist.org/sof",
                           body=open(BOSTON_SAMPLE_HTML, 'r').read(),
                           content_type="text/html")


def _setup_cities_responses():
    httpretty.register_uri(httpretty.GET, 
                           CITIES_URL,
                           body=open(US_SAMPLE_HTML, 'r').read(),
                           content_type="text/html")


@httpretty.activate
def test_find_all():
    _setup_mock_responses()
    categories, cities, keywords = ['sof'], ['boston'], ['']
    results = find(categories, keywords, cities)
    assert(len(results) == 1)
    assert(results[0].city == 'boston')
    assert(results[0].cat == 'sof')
    assert(len(results[0].items) == 4)


@httpretty.activate
def test_find_java():
    _setup_mock_responses()
    categories, cities, keywords = ['sof'], ['boston'], ['java']
    results = find(categories, keywords, cities)
    assert(len(results) == 1)
    assert(len(results[0].items) == 1)   
    item = results[0].items[0]
    assert(item.title=='JAVA Developer  (Boston near North and South Station)')
    assert(item.url=='http://boston.craigslist.org/gbs/sof/4286078333.html')


@httpretty.activate
def test_cities():
    _setup_cities_responses()
    _region = cities('US')
    assert(len(_region.states) == 52)    
    alabama = _region.states[0]
    assert(alabama.name == 'Alabama')
    assert(len(alabama.cities) == 9)
    tuscaloosa = alabama.cities[8]
    assert(tuscaloosa.name == 'tuscaloosa')
    assert(tuscaloosa.url == 'http://tuscaloosa.craigslist.org')
    territories = _region.states[51]
    assert(territories.name == 'Territories')
    assert(len(territories.cities) == 3)
