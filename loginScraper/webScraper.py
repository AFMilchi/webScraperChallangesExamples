#!/usr/bin/python
import webCrawler as wc
import dataExtractor as de
import dbConnector as dc


class WebScraper():
    def __init__(self):
        self.crawler = wc.WebCrawler()
        self.extractor = de.DataExtractor()
        self.connector = dc.DbConnector()
        self.allModules = set()

    def getAlLModuleLinks(self):
        for link in self.crawler.getStudiengaengeLinks('studiengaenge.html'):
            self.crawler.getInhalteLinks(link)

    def extractAllModules(self):
        for link in self.crawler.inhalteLinks:
            self.allModules.update(set(self.extractor.extractModules(link)))

    def writeModulesInDB(self):
        self.connector.writeOut(self.allModules)

    def getAllSemesterLinks(self):
        for link in self.crawler.getStudiengaengeLinks('studiengaenge.html'):
            self.crawler.getInhalteLinks(link)


if __name__ == "__main__":
    ws = WebScraper()
    ws.getAllSemesterLinks()
    # ws.getAlLModuleLinks()
    # ws.extractAllModules()
    # ws.writeModulesInDB()
