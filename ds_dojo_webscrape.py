"""
Intro to web scraping with beautiful soup
Data Science Dojo
https://www.youtube.com/watch?v=XQgXKtPSzUI
"""

from urllib.request import urlopen as uREq
from bs4 import BeautifulSoup as soup

my_url = 'http:www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%card'