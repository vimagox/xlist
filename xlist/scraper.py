import requests
from lxml import html
from settings import CITY_URL
from models import Item

_ITEM_PATH = '//p[@class="row"]'
_DATE_PATH = 'span[@class="pl"]/span[@class="date"]'
_TITLE_PATH = 'span[@class="pl"]/a'
_LINK_PATH = 'span[@class="pl"]/a/@href'
_DETAILS_PATH = 'span[@class="l2"]/span[@class="pnr"]/small'


class HtmlScraper(object):
    def __init__(self, text):
        """
        Html scraper
        :parse text: html text
        """
        self.tree = html.fromstring(text)
        self.item_paths = self.tree.xpath(_ITEM_PATH)

    def scrape_item(self, path, keywords):
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
        _title_details = '{} {}'.format(_title, _details)

        for keyword in keywords:
            if keyword.upper() in _title_details.upper():
                return Item(_date, _title_details, _link, keyword=keyword)
        return None
