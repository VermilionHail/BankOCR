

class OCR():

    def __init__(self, file):
        with open(file) as accounts:
            self.lines = accounts.readlines()