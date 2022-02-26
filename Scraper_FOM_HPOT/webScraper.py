#!/usr/bin/python
import webCrawler as wc
import dataExtractor as de
import dbConnector as dc


class WebScraper():
    '''Führt als Aggregation die einzelen Komponenten zusammen
    und dient als einstiegspunkt in den Scraper
    :param crawler: Crawler Komponente zum Sammeln von URLs
    :type crawler: WebCrawler
    :param extractor: Daten Extractor Komponente zum extrahieren von Daten
    :type extractor: DataExtracot
    :param connector: Anbindung an Datenbank
    :type connector: DbConnector
    :param allModules: Sammlung aller Module
    :type allModules: set'''

    def __init__(self):
        '''Konstructor'''
        self.crawler = wc.WebCrawler()
        self.extractor = de.DataExtractor()
        self.connector = dc.DbConnector()
        self.allModules = set()

    def getAlLModuleLinks(self):
        '''Lässt Crawler nach Studiengänge URLs
        und anschließend weiter nach Studiengang-Inhalts URLs suchen
        :rtype: void'''
        for link in self.crawler.getStudiengaengeLinks('/'):
            self.crawler.getInhalteLinks(link)
            ''' Abbruchbedingung zu Testzwecken, auskommentieren bei vollständigem Scraping
                Nach 3 gefunden Links wird abgebrochen da Vorgang sehr langsam'''
            if len(self.crawler.inhalteLinks) > 2:
                return

    def extractAllModules(self):
        '''Holt die vorab gesammelten Inhalte URLs, übgibt sie dem extractor
        und fügt die extrahierten Module dem allModules set hinzu
        :rtype: void'''
        for link in self.crawler.inhalteLinks:
            self.allModules.update(set(self.extractor.extractModules(link)))

    def writeModulesInDB(self):
        '''Schreibt den Inhalt von allModules
        :rtype: void'''
        self.connector.writeOut(self.allModules)


if __name__ == "__main__":
    '''Programmeinstiegspunkt'''
    ws = WebScraper()
    try:
        ws.getAlLModuleLinks()
    except:
        pass
    ws.extractAllModules()
    ws.writeModulesInDB()
