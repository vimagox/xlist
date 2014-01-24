"""
Functionality to find craigslist items by city and category
"""
from scraper import HtmlScraper
from models import CityItems
from settings import CITIES
import requests


def find_by_city(city, cat, keywords):
    """
    Find items by city
    :param city: city
    :param cat: category
    :param keywords: keywords
    """
    print "--------------------------------------------------------"
    city_items = CityItems(city, cat)
    r = requests.get(city_items.url)
    if r.status_code == 200:
        scraper = HtmlScraper(r.text)
        for path in scraper.item_paths:
            item = scraper.scrape_item(path, keywords)
            if item:
                print item
                city_items.add_item(item)
    else:
        print 'ERROR: Invalid city: {}'.format(city)
    return city_items


def find(categories, keywords, cities):
    """
    Finds craigslist data in different cities
    :param categories: List of craigslist categories (ie: sof - Software jobs)
    :param keywords: List of keywords to look for
    :para cities: List of cities to look into
    :returns: List of CityItems instances
    """
    results = []
    for city in cities:
        for cat in categories:
            city_items = find_by_city(city, cat, keywords)
            results.append(city_items)
    return results
