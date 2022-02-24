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
    :type allModules: set
    :param allOCModulesLecturer: Liste von Touples aller Module mit Dozenten
    :type allOCModulesLecturer: list'''

    def __init__(self):
        '''Konstructor'''
        self.crawler = wc.WebCrawler()
        self.extractor = de.DataExtractor()
        self.connector = dc.DbConnector()
        self.allModules = set()
        self.allOCModulesLecturer = list()

    def getAlLModuleLinks(self):
        '''Lässt Crawler nach Studiengänge URLs
        und anschließend weiter nach Studiengang-Inhalts URLs suchen
        :rtype: void'''
        for link in self.crawler.getStudiengaengeLinks('studiengaenge.html'):
            self.crawler.getInhalteLinks(link)

    def extractAllModules(self):
        '''Holt die vorab gesammelten Inhalte URLs, übgibt sie dem extractor
        und fügt die extrahierten Module dem allModules set hinzu
        :rtype: void'''
        for link in self.crawler.inhalteLinks:
            self.allModules.update(set(self.extractor.extractModules(link)))

    def writeDataInDb(self):
        '''Schreibt den Inhalt von allOCModulesLecturer'''
        self.connector.writeOut(self.allOCModulesLecturer)

    def ExtractAllOCModulesAndLecturer(self):
        '''Lässt Craler alle SemesterLinks Sammeln und lässt extracotr
        alle Module mit Dozenten aus den Links Sammeln und speichert
        sie in allOCModulesLecturer
        :rtype:void'''
        for link in self.crawler.getSemesterLinks('/nfcampus/Node.do?n=5220'):
            self.allOCModulesLecturer.extend(
                self.extractor.extractOCModulesAndLecturer(link))


if __name__ == "__main__":
    '''Programmeinstiegspunkt'''
    ws = WebScraper()
    ws.ExtractAllOCModulesAndLecturer()
    ws.writeDataInDb()
