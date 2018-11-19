 # -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import urllib2
import re

# Input URL
url=raw_input("Enter url\n")

# Get Domain
domain=url.split("//")[-1].split("/")[0]

# Get webpage
html_page = urllib2.urlopen(url)

# Get decoded response
response=html_page.read()

# Parse page for further analysis
soup = BeautifulSoup(response)

links = []

# Get all links matching to that domain
for link in soup.findAll('a', attrs={'href': re.compile(domain)}):
    links.append(link.get('href'))

# Output details
print("The number of links in webpage pointing to same domain is "+str(len(links)))
print("The size of webpage in bytes is "+str(len(response)))
