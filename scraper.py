import requests
from bs4 import BeautifulSoup


base_url = "http://newyork.craigslist.org"
file_paths = []

#PART 1 - get all the file paths

#use requests to grab the raw data  from craigslist
r = requests.get("http://newyork.craigslist.org/search/sss?query=mirror&s=200")
# print r.content #r.content shows us html of page

soup = BeautifulSoup(r.content)
# print soup.prettify
listings = soup.find_all("p", class_="row") #find all p tags with class row
# images = listings.find_all("a");

for item in listings: #for each listing, get the a tag
    links = item.find_all("a");
    for link in links:
      path = link['href'] #get the href from each a tag, this is the path to each listing
      file_paths.append(base_url + path) #add to a list of all the file paths

for url in file_paths:
    print url #print each url individually



#PART 2 - scrape the image from each individual page