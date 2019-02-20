"""
Codecademy Web Scraping with Python Webinar Notes

hackernews.com

"""

import requests
# pip install bs4
from bs4 import BeuatifulSoup 

res = requests.get(https://news.ycombinator.com/)

soup = BeutifulSoup(res.content. 'html.parser')

# need to find the html tags to scrape

# webinar cut off will get remaining code soon
