import requests
from bs4 import BeautifulSoup
import urllib.robotparser
import time


class WebLoader():
    '''Kümmert sich um den Download von Webseiten
    :param url: URL der herunterzuladenen Website
    :type url: string
    :param rp: Parser für robots.txt Dateien
    :type rp: robotFileParser
    :param crawlDelay: Wartewert zwischen zwei HTTP Requests
    :type crawlDelay: int
    '''

    def __init__(self, url):
        '''Konstruktor, beim erzeugen des Objektes wird
        Website bereits runtergeladen. Die Robots.txt wird ausgewertet
        und der CrawlDelay (default 0) bestimmt.
        :param url: URL der herunterzuladenen Website
        :type url: string'''
        self.url = url
        self.rp = urllib.robotparser.RobotFileParser()
        self.rp.set_url('https://www.fom.de/robots.txt')
        self.rp.read()
        self.crawlDelay = self.rp.crawl_delay('*')
        if self.crawlDelay is None:
            self.crawlDelay = 0
        self.getPage(url)

    def getPage(self, url):
        '''Methode die nur Klassenintern genutzt wird
        zum herunterladen der Website. Jede URL wird vor dem Download
        überprüft ob sie in Robots.txt erlaubt ist.
        :param url: URL der Website
        :type url: string'''
        if self.rp.can_fetch('*', url):
            print(self.rp.can_fetch('*', url))
            self.page = requests.get(url)
            time.sleep(self.crawlDelay)
        else:
            self.page = ''

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
