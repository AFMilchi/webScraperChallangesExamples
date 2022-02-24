import requests
import json
from bs4 import BeautifulSoup


class WebLoader():
    def __init__(self, url):
        self.url = url
        # self.getPage(url)
        self.getPageWithLogin(url)

    def getPage(self, url):
        self.page = requests.get(url)

    def getPageWithLogin(self, url):
        '''Logs into OC and returns Page from Input URL'''
        login_url = 'https://campus.bildungscentrum.de/nfcampus/Login.do'
        credentials = self.getCredentials()

        with requests.Session() as session:
            session.post(login_url, data=credentials)
            page = session.get(url)
        self.page = page

    def getCredentials(self):
        '''Credentials should be located at directory meta withing Projektfolder'''
        with open('../meta/credentials.json', 'r') as file:
            credentials = json.load(file)
            return credentials

    def getHTMLText(self):
        return self.page.text

    def getBSObject(self):
        return BeautifulSoup(self.page.text, 'html.parser')
