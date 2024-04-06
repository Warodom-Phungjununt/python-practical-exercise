# PART 1
# Libraries for this lab
# urllib.parse: arrange the form of URL
# requests: control HTTP Requests open and read webpage form URL
# BeautifulSoup: process and organize data from HTML files
# sleep: stop processing for the specified period of time (seconds)
# copy: copy object

import requests
import urllib.parse
from bs4 import BeautifulSoup
from time import sleep
import copy

# Reading HTML from URL
# Before starting the process, We need to send a request to the URL to request the HTML file of the web page with the command requests.get()
response = requests.get('https://th.wikipedia.org/w/index.php?title=จีดีเอช&oldid=8244422')
print(response)
print(response.status_code, response.reason)
print(response.headers)
# When receiving the right response, "text" operation to read HTML can be used
html = response.text
print(html[0:500])
# Once you have an HTML page that is ready to use can be used BeautifulSoup To continue processing the HTML pages that are obtained.
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify()[0:500])