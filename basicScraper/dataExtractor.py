from webLoader import WebLoader
from bs4 import BeautifulSoup


class DataExtractor:
    def __init__(self):
        pass

    def extractModules(self, url):
        page = WebLoader('https://fom.de/'+url).getBSObject()
        tableContents = page.find('table', class_='inhalte').find_all('p')

        for element in tableContents:
            '''
            element.text can look like one of those 4:
            7. Semester
            Operatives Controlling (7 CP)
            6. SemesterWertschöpfungsmanagement (5 CP)
            Go Internationale!
            '''
            pass
        # remove entries without 'CP)' in them
        bufferlist = [x.text for x in tableContents if 'CP)' in x.text]
        # remove the trailing (x CP)
        bufferlist2 = [x.split(' (')[0] for x in bufferlist]
        # remove weirdly formated 'x. Semester' in beginning of line
        moduleList = [x.split(' Semester')[1]
                      if ' Semester' in x else x for x in bufferlist2]
        return set(moduleList)
