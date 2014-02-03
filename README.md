xlist
=====
Find craigslist stuff in different cities


## setup

	pip install -r requirements.txt;pip install -r requirements_dev.txt;


	installing lxml in ubuntu requires:

	"""
	sudo apt-get install libxml2-dev libxslt-dev
	sudo apt-get install python-lxml
	"""

## Usage

### Command line interface

xlist command line currently supports 1 command, find

```	
python xlist.py find -X "sof,web" -K "python,javascript" -C boston

Args:
	-X, --categories	Craigslist categories (sof for software jobs - http://city.craigslist.org/sof)
	-K, --keywords      Keywords/Search to look for; comma separated string.
	-C, --cities		Specific cities to search

	All arguments are required.
```

### REST Service

Start the rest services
```
python app.py
```

Retrieve available craigslist cities
```
curl -u admin:admin http://localhost:8080/region/us/cities
```

Retrieve items from a specific city/category/keyword:

```	
curl -u admin:admin http://localhost:8080/boston/sof?k=python

k - Comma separated list of keywords
c - Comma separated list of cities
```


### Testing

```
nosetests -c .noserc_local
```

Then check `test_results/coverage/index.html` for the HTML report.
