class DbConnector:
    '''Simuliert eine Interface Klasse zu einer Datenbank o.ä'''

    def __init__(self):
        '''Konstruktor'''
        pass

    def writeOut(self, data):
        ''' Nimmt daten und schreibt sie in Textdatei

        :param data: Die zu schreibenden Daten
        :type url: iterable (list, set, usw)
        :rtype: int
        :return: 0 bei erfolg, -1 bei miserfolg
        '''
        try:
            with open('./moduleList.txt', 'w') as file:
                for element in data:
                    file.writelines(str(element)+'\n')
        except IOError:
            print('error occured')
            return -1
        return 0
