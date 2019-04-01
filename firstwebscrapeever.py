from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


my_url = 'https://www.newegg.com/global/au-en/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=gpu&N=-1&isNodeId=1'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.findAll("div", {"class": "item-container"})

filename = "products.csv"
f = open(filename, "w")
headers = "brand \n"
f.write(headers)
# container = containers[0].img["title"]
# container = containers[0]

# brand = page_soup.findAll("div", {"class" : "item-info"})
# Check amount len(brand)

# Only works from index 4+
# brand[4].div.a.img["title"]
# containers.findAll("li",{"class":"price-ship"})
i = 1

for container in containers:
    brand = container.img["title"]

    print(i)
    print(brand)
    i += 1

    f.write(brand + "\n")

f.close()
