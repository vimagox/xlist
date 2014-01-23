"""
Functionality to find craigslist items by city and category
"""
import requests
from lxml import html
from settings import CITY_URL


_ITEM_PATH = '//p[@class="row"]'
_DATE_PATH = 'span[@class="pl"]/span[@class="date"]'
_TITLE_PATH = 'span[@class="pl"]/a'
_LINK_PATH = 'span[@class="pl"]/a/@href'
_DETAILS_PATH = 'span[@class="l2"]/span[@class="pnr"]/small'


class CityFindings(object):
    def __init__(self, city, cat):
        self.city = city
        self.cat = cat
        self.url = CITY_URL.format(city, cat)
        self.findings = []

    def finding_link(self, value):
        if value.startswith('http'):
            return value
        prefix = self.url[0: -(len(self.cat)+1)]
        return '{}{}'.format(prefix, value)

    def __str__(self):
        return '{} ({})'.format(self.city, self.cat)


class Finding(object):
    def __init__(self, date, title, link, keyword):
        self.date = date
        self.title = title
        self.link = link
        self.keyword = keyword

    def __str__(self):
        return '[{}] {}: {}'.format(self.date, self.keyword, self.title)


def _finding(path, keywords):
    """
    Returns an Item instance when keywords are found
    :param path: item xpath
    :param keywords: search keywords
    """
    _date = path.findtext(_DATE_PATH)
    _title = path.findtext(_TITLE_PATH).encode('ascii', 'ignore')
    _link = path.xpath(_LINK_PATH)[0]
    _details = path.findtext(_DETAILS_PATH)
    _details = _details.encode('ascii', 'ignore') if _details else ''
    _title_details = '{} ({})'.format(_title, _details)

    for keyword in keywords:
        if keyword.upper() in _title_details.upper():
            return Finding(_date, _title_details, _link, keyword=keyword)
    return None


def find(categories, keywords, cities):
    """
    Finds craigslist data in different cities
    :param categories: List of craigslist categories (ie: sof - Software jobs)
    :param keywords: List of keywords to look for
    :para cities: List of cities to look into
    :returns findings: List of CityFindings instances
    """
    results = []
    for city in cities:
        for cat in categories:
            print "--------------------------------------------------------"
            city_findings = CityFindings(city, cat)
            results.append(city_findings)
            print city_findings.url
            r = requests.get(city_findings.url)
            if r.status_code == 200:
                _tree = html.fromstring(r.text)
                _item_paths = _tree.xpath(_ITEM_PATH)
                for _path in _item_paths:
                    finding = _finding(_path, keywords)
                    if finding:
                        finding.link = city_findings.finding_link(finding.link)
                        print '{} - {}'.format(finding, finding.link)
                        city_findings.findings.append(finding)
            else:
                print 'ERROR: Invalid city: {}'.format(city)
    return results
