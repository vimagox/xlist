"""
xlist models
"""

class CityItems(object):
    def __init__(self, city, cat):
        self.city = city
        self.cat = cat
        self.url = CITY_URL.format(city, cat)
        self.items = []

    def add_item(self, item):
        item.link = self._build_item_link(item.link)
        self.items.append(item)

    def _build_item_link(self, value):
        if value.startswith('http'):
            return value
        prefix = self.url[0: -(len(self.cat)+1)]
        return '{}{}'.format(prefix, value)

    def __str__(self):
        return '{} ({})'.format(self.city, self.cat)


class Item(object):
    def __init__(self, date, title, link, keyword):
        self.date = date
        self.title = title
        self.link = link
        self.keyword = keyword

    def __str__(self):
        return '[{}] {}: {}'.format(self.date, self.keyword, self.title)
