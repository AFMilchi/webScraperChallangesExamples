from webLoader import WebLoader


class DataExtractor:
    '''Klasse welche sich mit dem extrahieren von Informatinen
    aus Websites beschäftigt'''

    def extractModules(self, url):
        '''Lädt Seite unter gegebener URL und extrahiert alle Modulnamen

        :param url: url eines Studienganges
        :type url: string
        :rtype: set
        :return: Ein set von Strings der Modulnamen
        '''
        page = WebLoader('https://fom.de/'+url).getBSObject()
        tableContents = page.find('table', class_='inhalte').find_all('p')

        '''
        tableContents.text sieht wie eine dieser Zeilen aus:
        7. Semester
        Operatives Controlling (7 CP)
        6. SemesterWertschöpfungsmanagement (5 CP)
        Go Internationale!
        '''
        # Löscht Zeilen ohne 'CP)'
        bufferlist = [x.text for x in tableContents if 'CP)' in x.text]
        # Löscht '(X CP)' am Zeilenende
        bufferlist2 = [x.split(' (')[0] for x in bufferlist]
        # Verarbeitet schlecht formatierte Zeilen mit 'x. SemesterModulname'
        moduleList = [x.split(' Semester')[1]
                      if ' Semester' in x else x for x in bufferlist2]
        return set(moduleList)
