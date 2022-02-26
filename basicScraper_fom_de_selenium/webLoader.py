from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
# Pfad ist ans System anzupassen
# Windows z.B: PATH = 'C:\Program Files (x86)\chromedriver.exe'
PATH = 'chromedriver'


class WebLoader():
    '''Kümmert sich um den Download von Webseiten
    :param url: URL der herunterzuladenen Website
    :type url: string
    :param driver: Steuerung des Selenium/Chrome Browsers
    :type driver: selenium.webdriver.chrome.webdriver.WebDriver
    '''

    def __init__(self, url):
        '''Konstruktor, beim erzeugen des Objektes wird
        Webdriver erzeugt und Website bereits im Browser aufgerufen
        :param url: URL der herunterzuladenen Website
        :type url: string'''
        self.url = url
        self.driver = webdriver.Chrome(executable_path=PATH)
        self.getPage(url)

    def getPage(self, url):
        '''Methode die nur Klassenintern genutzt wird
        zum herunterladen der Website
        :param url: URL der Website
        :type url: string'''
        self.page = self.driver.get(url)

    def getHTMLText(self):
        '''Liefert die Website als HTML Text
        :return: page als HTML Text
        :rtype: string'''
        return self.page.text

    def getSeleniumDriver(self):
        '''Liefer die Website als Selenium webdriver Object
        :return: Driver Object des Browsers
        :rtype: WebDriver'''
        return self.driver
