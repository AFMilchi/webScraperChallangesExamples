import requests
from bs4 import BeautifulSoup


class WebLoader():
    def __init__(self, url):
        self.url = url
        self._getPage(url)

    def _getPage(self, url):
        self.page = requests.get(url)

    def getHTMLText(self):
        return self.page.text

    def getBSObject(self):
        return BeautifulSoup(self.page.text, 'html.parser')
