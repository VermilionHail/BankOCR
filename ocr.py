

class OCR():

    def __init__(self, file):
        self.lines = self.read_lines(file)

    def read_lines(self, file):
        with open(file) as accounts:
            lines = accounts.readlines()
        #remove end of line characters
        for i in range(len(lines)):
            lines[i] = lines[i].replace('\n', '') 
        return lines