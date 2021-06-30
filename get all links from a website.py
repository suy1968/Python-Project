import requests
from bs4 import BeautifulSoup
def get_links(url):
    links = []
    website = requests.get(url)
    website_text = website.text
    Soup = BeautifulSoup(website_text)
    for link in Soup.find_all('a'):
        links.append(link.get('href'))            #< a href = 'link'>
    for link in links:
        print(link)
        print(len(links))
get_links('https://www.bplans.com/')
get_links('https://www.geeksforgeeks.org/')
