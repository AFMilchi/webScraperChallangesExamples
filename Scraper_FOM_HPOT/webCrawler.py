from webLoader import WebLoader


class WebCrawler:
    '''Kümmert sich um das durchforsten von Websites und Sammeln von URLs

    :param studiengaengeLinks: Sammlung aller URLs von Studiengängen
    :type studiengaengeLinks: set
    :param inhalteLinks: Sammlung aller URLs von Studiengangsverlaufsinhalten
    :type inhalteLinks: set
    '''

    def __init__(self):
        '''Konstruktor'''
        self.studiengaengeLinks = set()
        self.inhalteLinks = set()

    def getStudiengaengeLinks(self, url):
        '''Sammelt unter gegebene URL nach URLs von Studiengängen

        :param url: Startpunkturl auf der fom.de Seite
        :type url: string
        :rtype: set
        :return: Ein set von Strings der Studiengangs URLs
        '''
        driver = WebLoader('https://www.fom.de/'+url).getSeleniumDriver()
        # findet alle <a> Tags wo 'studiengaenge' im Link Namen ist
        for element in driver.find_elements_by_tag_name('a'):
            href = element.get_attribute('href')
            if href is not None and '/studiengaenge/' in href:
                self.studiengaengeLinks.add(href)
        driver.close()
        return self.studiengaengeLinks

    def getInhalteLinks(self, url):
        '''Sammelt unter gegebener URL nach URLs von Studiengangsinhalten
         und schreibt sie in Attribut self.inhalteLinks.
         Jeder Hyperlink wird überprüft ob er überhaupt sichtbar ist

        :param url: URL eines Studiengangs
        :type url: string
        :rtype: void
        '''
        driver = WebLoader(url).getSeleniumDriver()
        for element in driver.find_elements_by_tag_name('a'):
            href = element.get_attribute('href')
            if href is not None and 'inhalte.html' in href and element.is_displayed():
                print(href)
                self.inhalteLinks.add(href)
                # beschleunigt Vorgang, da nur 1 inhalte.html pro Studiengang vorhanden
                return
