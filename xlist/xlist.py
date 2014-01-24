"""
Command line tool to scrape and parse craigslist cities
"""
import argparse
from services import find
from settings import CITIES


def create_main_parser():
    parser = argparse.ArgumentParser(
        description='Scrape craigslist data in different cities',
        prog='craigslist'
    )

    subparsers = parser.add_subparsers(
        title='commands',
        help='valid commands',
        dest='command'
    )
    return parser, subparsers


def create_find_parser(subparsers):
    parser_find = subparsers.add_parser(
        'find', help='Find stuff in craigslist'
    )
    parser_find.add_argument(
        '-X', '--categories', type=str, required=True,
        help='Craigslist category (ie. "sof,web" - for software/web jobs - http://city.craigslist.org/category)'
    )    
    parser_find.add_argument(
        '-K', '--keywords', type=str, required=True,
        help='Keywords to search for (ie. "java,groovy")'
    )
    parser_find.add_argument(
        '-C', '--cities', type=str, required=False,
        help='Cities to search.'
    )

    return parser_find


def _list(value):
    return [x.strip() for x in value.split(',')]


def main():
    parser, subparsers = create_main_parser()
    create_find_parser(subparsers)

    args = parser.parse_args()

    if args.command == 'find':
        cats = _list(args.categories)
        keywords = _list(args.keywords)
        cities = _list(args.cities) if args.cities else CITIES
        
        try:
            find(cats, keywords, cities)
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    main()