import unittest
from ocr import OCR

class TestOCR(unittest.TestCase):

    def setUp(self):
        self.ocr = OCR('AccountNumbers.txt')
    
    def test_LinesReadFromFileAreMultipleOfFour(self):
        self.assertNotEqual(len(self.ocr.lines), 0) #make sure lines isn't empty
        self.assertEqual(len(self.ocr.lines) % 4, 0) #make sure formatting of each entry is the correct length
    
    def test_EveryFourthLineShouldBeBlank(self):
        multiple_of_four_line = []
        for i in range(3, len(self.ocr.lines)):
            if (i + 1) % 4 == 0:
                multiple_of_four_line.append(self.ocr.lines[i])
                print(multiple_of_four_line)
        for j in range(len(multiple_of_four_line)):
            self.assertNotEqual(len(multiple_of_four_line[j]), 0) #make sure line wasn't already empty
            multiple_of_four_line[j] = multiple_of_four_line[j].replace(' ', '') 
            self.assertEqual(len(multiple_of_four_line[j]), 0)

if __name__ == "__main__":
    unittest.main()