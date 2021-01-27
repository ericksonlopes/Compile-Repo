import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(requests.get('https://github.com/docker/compose').content, 'html.parser')

soup = soup.find(
    class_='Details-content--hidden-not-important js-navigation-container js-active-navigation-container d-md-block')

for item in soup.find_all(role="rowheader"):
    print(item, '\n')

# 'Details-content--hidden-not-important js-navigation-container js-active-navigation-container d-md-block'
#
# "Details-content--hidden-not-important js-navigation-container js-active-navigation-container d-md-block"
#
# 'Details-content--hidden-not-important js-navigation-container js-active-navigation-container d-block'
