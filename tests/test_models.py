"""
models tests
"""
from xlist.models import CityItems, Item


def test_city_items():
	city = CityItems('elpaso', 'sof')
	item = Item('Jan 13', 'Something here', '/abc/sof/xyz.html', 'something')
	city.add_item(item)

	assert(len(city.items)==1)
	assert(city.items[0].link == 'http://elpaso.craigslist.org/abc/sof/xyz.html')
