"""
Functionality to find craigslist items by city and category
"""
from scraper import HtmlScraper, CitiesScraper
from models import CityItems, Region
from settings import CITIES_URL
import requests


def cities(region):
    """
    Provide craigslist cities for the given region
    :param region: region
    :returns region: Region instance
    """
    states = []
    r = requests.get(CITIES_URL.format(region))
    if r.status_code == 200:
        scraper = CitiesScraper(r.text)
        for path in scraper.item_paths:
            state = scraper.scrape_state(path)
            states.append(state)
    else:
        print 'ERROR: Invalid city: {}'.format(city)
    return Region(region, states)


def find_by_city(city, cat, keywords):
    """
    Find items by city
    :param city: city
    :param cat: category
    :param keywords: keywords
    """
    print('----------------------{}:{}-------------------------'.format(city, cat))
    city_items = CityItems(city, cat, keywords)
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
