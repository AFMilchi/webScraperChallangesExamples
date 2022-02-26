import requests
import json
from bs4 import BeautifulSoup


class WebLoader():
    '''Kümmert sich um den Download von Webseiten
    :param url: URL der herunterzuladenen Website
    :type url: string
    '''

    def __init__(self, url):
        '''Konstruktor, beim erzeugen des Objektes wird
        Website bereits runtergeladen
        :param url: URL der herunterzuladenen Website
        :type url: string'''

        self.url = url
        self.getPageWithLogin(url)

    def getPageWithLogin(self, url):
        '''Methode die nur Klassenintern genutzt wird
        zum herunterladen der Website mit vorherigem Login
        :param url: URL der Website
        :type url: string
        '''
        login_url = 'https://campus.bildungscentrum.de/nfcampus/Login.do'
        credentials = self.getCredentials()

        with requests.Session() as session:
            # Logindaten werden als HTTP Post gesendet
            session.post(login_url, data=credentials)
            page = session.get(url)
        self.page = page

    def getCredentials(self):
        '''Holt die Anmeldedaten aus der Json Datei
        :return: OnlineCampus Anmeldedaten
        :rtype: dict
        '''
        with open('../meta/credentials.json', 'r') as file:
            credentials = json.load(file)
            return credentials

    def getHTMLText(self):
        '''Liefert die Website als HTML Text
        :return: page als HTML Text
        :rtype: string'''
        return self.page.text

    def getBSObject(self):
        '''Liefert die WEbsite als BS Object
        :return: page als BS Object
        :rtype: bs4.BeautifulSoup'''
        return BeautifulSoup(self.page.text, 'html.parser')
