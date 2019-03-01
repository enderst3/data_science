"""
Intro to web scraping with beautiful soup
Data Science Dojo
https://www.youtube.com/watch?v=XQgXKtPSzUI
"""

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%card"

# opening up connection, grabibng the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.findAll('div', {"class":"item-container"})

filename = 'products.csv'
f = open(filename, 'w')

headers = "brand, product_name, shipping\n"

f.write(headers)

for container in containers:
    brand = container.img["title"]

    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text
    
    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)

    f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")

f.close()