import unittest
import requests
from lxml import html


CRAIGSLIST_URL = 'http://{}.craigslist.org/sof'

def scrape(url):
	r = requests.get(url)
	return r.status_code, r.text

# reading lines like any other language
def read_lines2(text):
	lines = []
	for line in text.split('\n'):
		lines.append(line)
	return lines

# reading lines the python way (list comprehensions)
def read_lines(text):
	return [line for line in text.split('\n')]

def test_scraper():
	cities = ['boston']
	for city in cities:
		status, text = scrape(CRAIGSLIST_URL.format(city))
		assert(status == 200)
		tree = html.fromstring(text)
		# print tree.xpath('//div[@class="content"]/h4/span/text()')
		print tree.xpath('//p[@class="row"]/text()')
		# lines = read_lines(text)
		# for line in lines:
		# 	if 'JAVA' in line:
		# 		# idx = line.index('</a>')
		# 		# print line[0:idx]
		# 		print line

 # <p class="row" data-pid="4285756647"> 
 # 	<a href="/gbs/sof/4285756647.html" class="i"></a> 
 # 	<span class="star"></span> 
 # 	<span class="pl"> 
 # 		<span class="date">Jan 13</span>  
 # 			<a href="/gbs/sof/4285756647.html">
 # 				Back-End JAVA Web Platform Development 
 # 			</a> 
 # 		</span> 
 # 		<span class="l2">   
 # 		<span class="pnr"> 
 # 			<small> (Boston)</small> 
 # 			<span class="px"> 
 # 				<span class="p"> </span>
 # 			</span> 
 # 		</span>  
 # 	</span> 
 # </p>