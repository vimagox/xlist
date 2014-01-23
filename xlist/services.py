"""
Functionality to find craigslist items by city and category
"""

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
            city_items = CityItems(city, cat)
            results.append(city_items)
            print city_items.url
            r = requests.get(city_items.url)
            if r.status_code == 200:
                scraper = HtmlScraper(r.text)
                for path in scraper.item_paths():
                    item = scraper.scrape_item(path, keywords)
                    if item:
                        print item
                        city_items.add_item(item)
            else:
                print 'ERROR: Invalid city: {}'.format(city)
    return results
