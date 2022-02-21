class DbConnector:
    def __init__(self):
        pass

    def writeOut(self, data):
        with open('./moduleList.txt', 'w') as file:
            for element in data:
                file.writelines(str(element)+'\n')
