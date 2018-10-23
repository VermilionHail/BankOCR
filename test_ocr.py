import unittest
from ocr import OCR

class TestOCR(unittest.TestCase):

    def setUp(self):
        self.ocr = OCR('AccountNumbers.txt')
    
    def test_LinesReadFromFileAreMultipleOfFour(self):
        self.assertNotEqual(len(self.ocr.lines), 0) #make sure lines isn't empty
        self.assertEqual(len(self.ocr.lines) % 4, 0) #make sure formatting of each entry is the corret length
    

if __name__ == "__main__":
    unittest.main()