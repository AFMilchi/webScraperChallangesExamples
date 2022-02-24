from webLoader import WebLoader
import re


class WebCrawler:
    '''Kümmert sich um das durchforsten von Websites und Sammeln von URLs

    :param studiengaengeLinks: Sammlung aller URLs von Studiengängen
    :type studiengaengeLinks: set
    :param inhalteLinks: Sammlung aller URLs von Studiengangsverlaufsinhalten
    :type inhalteLinks: set
    :param semesterLinks: Sammlung aller URLs von Semestern
    :type semesterLinks: set
    '''

    def __init__(self):
        '''Konstruktor'''
        self.studiengaengeLinks = set()
        self.inhalteLinks = set()
        self.semesterLinks = set()

    def getStudiengaengeLinks(self, url):
        '''Sammelt unter gegebene URL nach URLs von Studiengängen

        :param url: Startpunkturl auf der fom.de Seite
        :type url: string
        :rtype: set
        :return: Ein set von Strings der Studiengangs URLs
        '''
        bs = WebLoader('https://www.fom.de/'+url).getBSObject()
        # findet alle <a> Tags wo 'studiengaenge' im Link Namen ist
        for link in bs.find_all('a', href=re.compile('studiengaenge/')):
            if 'href' in link.attrs:
                self.studiengaengeLinks.add(link.attrs['href'])
        return self.studiengaengeLinks

    def getInhalteLinks(self, url):
        '''Sammelt unter gegebener URL nach URLs von Studiengangsinhalten
         und schreibt sie in Attribut self.inhalteLinks

        :param url: URL eines Studiengangs
        :type url: string
        :rtype: void
        '''
        bs = WebLoader('https://www.fom.de/'+url).getBSObject()
        for link in bs.find_all('a', href=re.compile('inhalte.html$')):
            if 'href' in link.attrs:
                self.inhalteLinks.add(link.attrs['href'])

    def getSemesterLinks(self, url):
        '''Sammelt unter gegebener URL nach URLs von Semestern im OnlineCampus

        :param url: URL eines Studiengangs
        :type url: string
        :rtype: set
        :return: Set von Strings der Semester URLs
        '''
        bs = WebLoader('https://campus.bildungscentrum.de'+url).getBSObject()
        for link in bs.find_all('a', href=re.compile('semester=')):
            if 'href' in link.attrs:
                self.semesterLinks.add(link.attrs['href'])
        return self.semesterLinks
