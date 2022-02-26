import requests
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
        self.getPage(url)

    def getPage(self, url):
        '''Methode die nur Klassenintern genutzt wird
        zum herunterladen der Website
        :param url: URL der Website
        :type url: string'''
        self.page = requests.get(url)

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
