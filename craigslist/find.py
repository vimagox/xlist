import argparse
import requests
from lxml import html


SCREEN_OUTPUT = 'screen'
HTML_OUTPUT = 'html'


CRAIGSLIST_CITY_URL = 'http://{}.craigslist.org/{}'


def find(categories, keywords, cities, output):
	"""
	Finds craigslist data in different cities
	:param categories: List of craigslist categories (ie: sof for Software jobs)
	:param keywords: List of keywords to look for
	:para cities: List of cities to look into
	:param output: Desired output format (options: screen/html)
	"""
	for city in cities:
		for cat in categories:
			print "---------------------------------------------------------------------"
			city_url = CRAIGSLIST_CITY_URL.format(city, cat)
			print '>>Looking in {}'.format(city_url)
			r = requests.get(city_url)
			if r.status_code == 200:
				tree = html.fromstring(r.text)
				# jobs = tree.xpath('//p[@class="row"]/span[@class="pl"]/a/text()') 
				jobs = tree.xpath('//p[@class="row"]') 
				for job in jobs:
					_date = job.findtext('span[@class="pl"]/span[@class="date"]')
					_title = job.findtext('span[@class="pl"]/a')
					_details = job.findtext('span[@class="l2"]/span[@class="pnr"]/small')
		 			for keyword in keywords:
		 				_title_match = keyword.upper() in _title.upper()
		 				_details_match = keyword in _details.upper() if _details else False
		 				if _title_match or _details_match:
		 					try:
		 						if output == SCREEN_OUTPUT:
		 							print '----[{}] {} : {} - {}'.format(_date, keyword, _title, _details or '')
		 						break
		 					except Exception:
		 						#UnicodeEncodeError: 'ascii' codec can't encode character u'\u200b' in position 0: ordinal not in range(128)
		 						print 'ERROR: Unable to display a job in {}'.format(city)
			else:
				print 'ERROR: Unable to find city: {}'.format(city)

# <div class="content">
#     <p class="row" data-pid="4285320206"> 
#     	<a href="/gbs/sof/4285320206.html" class="i"></a> 
#     	<span class="star"></span> 
#     	<span class="pl"> 
#     		<span class="date">Jan 13</span>  
#     		<a href="/gbs/sof/4285320206.html">API Backend Node.js Software Developer</a> 
#         </span> 
#     	<span class="l2">   
#     		<span class="pnr"> <small> (allows remote)</small> 
#     			<span class="px"> 
#     				<span class="p"> </span>
#     			</span> 
#     		</span>  
#     	</span> 
#     </p> 
