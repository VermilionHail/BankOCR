#%%
with open('AccountNumbers.txt') as file:
    for line in file.readlines():
        print(line)

#%%
test_line = "   "
print(test_line)
print("Original length: " + str(len(test_line)))
test_line = test_line.replace(' ', '')
print(test_line)
print("Replaced length: " + str(len(test_line)))

#%%
from ocr import OCR

ocr = OCR('AccountNumbers.txt')
for line in ocr.lines:
    print(line)
    