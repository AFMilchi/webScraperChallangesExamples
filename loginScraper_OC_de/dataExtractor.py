from webLoader import WebLoader


class DataExtractor:
    '''Klasse welche sich mit dem extrahieren von Informatinen
    aus Websites beschäftigt'''

    def extractModules(self, url):
        '''Lädt Seite von fom.de unter gegebener URL und extrahiert
        alle Modulnamen

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

    def extractOCModulesAndLecturer(self, url):
        '''Lädt Seite vom OnlineCampus unter gegebener URL
         und extrahiert alle Modulnamen mit Dozenten

        :param url: url eines Semesters
        :type url: string
        :rtype: list(touple)
        :return: Eine Liste von Tuples mit (Modulname, Dozentname)
        '''
        page = WebLoader('https://campus.bildungscentrum.de'+url).getBSObject()
        tableContents = page.find(
            'table', class_='tablesorter hover-highlight').find_all('td')

        '''Jede Line sieht so aus (mit Leerzeichen und Leerzeilen)
            FOM
            User Experience - Ergonomie (M)

                                                        Hoffmann, Peter




            '''
        listOfLines = list()
        # entfernt alle Leerzeilen, Leerzeichen und Zeilen nur mit "FOM"
        for line in tableContents:
            stripedLine = line.text.strip().strip('FOM').strip('\n')
            if stripedLine != '':
                listOfLines.append(stripedLine)
        # Kombiniert alle 2er Pärchen der Liste zu einem Tuple und erzeugt daraus eine Liste
        moduleLectureTupleList = [(listOfLines[i], listOfLines[i+1])
                                  for i in range(0, len(listOfLines)-1, 2)]
        return moduleLectureTupleList
