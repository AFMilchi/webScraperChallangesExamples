import requests
import time
import secrets
from bs4 import BeautifulSoup


class WebLoader():
    '''Kümmert sich um den Download von Webseiten
    :param url: URL der herunterzuladenen Website
    :type url: string
    :param headers: Typische HTTP Header eines Clients
    :type headers: string
    '''

    def __init__(self, url):
        '''Konstruktor, beim erzeugen des Objektes wird
        Website bereits runtergeladen
        :param url: URL der herunterzuladenen Website
        :type url: string'''
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.105 Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;'
                        'q=0.9,image/webp,*/*;q=0.8'}
        self.getPage(url)

    def getPage(self, url):
        '''Methode die nur Klassenintern genutzt wird
        zum herunterladen der Website. Es werden typische Header gesetzt
        und mit dem HTTP GET gesendet. Nach jedem Request wird zufälligt
        zwischen 0,001s und 1s gewartet.
        :param url: URL der Website
        :type url: string'''
        crawlDelay = float(secrets.randbelow(1000)) * 0.001
        self.page = requests.get(url, headers=self.headers)
        time.sleep(crawlDelay)

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
