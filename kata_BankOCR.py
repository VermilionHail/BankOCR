import pandas as pd

#There are 10 possible digits each position can have, 0-9
#Initialize all entries to zero for the ten possible digits in each position
zeros = [0]*10 

#Make a series for each of the positions in the account number, 9 positions in total
seriesList = []
for i in range(0,9):
    colName = 'p' + str(9-i) #Names of positions have 9 on the left digit, and 1 on the right
    seriesList.append( pd.Series(zeros, name = colName) )

#Make seven copies of the dataFrame, one for each position in a digit that could have an underscore or pipe
frameList = []
for i in range(0,7):
    frameList.append(pd.DataFrame(seriesList).T)

#Read in the text file containing the account numbers
lines = []
with open('C:\\Programming\\Python\\katas\\BankOCR\\AccountNumbers.txt') as inputFile:
    for row in inputFile:
        lines.append(row)

#Find out how many account numbers are in the file. Each number has 3 lines of characters and one blank line
numEntries = int(len(lines)/4)
print(str(numEntries) + ' account numbers in this text file!')

class Accounts:
    def __init__(self, validity = 'OK', nums = []):
        codes = ['OK', 'ERR', 'ILL', 'AMB']
        if validity not in codes:
            raise ValueError('Please enter a valid account label code!')
        self.validity = validity
        self.accountNums = len(nums)
        self.accounts = nums    #should this be .append(nums) ???? I want .accounts to be a list of lists

    def add_accountNum(self, newNum): #This is most likely not necessary with how I have initialized the object
        self.accounts.append(newNum)
        self.accountNums += 1
        self.validity = 'AMB'

#Terrible sorting of what characters correspond to what possible numbers. Fix this!!!!!!!!!!!
def r1c2Func(character):
    possibleNums = {' ':[1,4],'|':[], '_':[0,2,3,5,6,7,8,9]}
    return possibleNums[character]

def r2c1Func(character):
    possibleNums = {' ':[1,2,3,7],'|':[0,4,5,6,8,9], '_':[]}
    return possibleNums[character]

def r2c2Func(character):
    possibleNums = {' ':[0,1,7],'|':[], '_':[2,3,4,5,6,8,9]}
    return possibleNums[character]

def r2c3Func(character):
    possibleNums = {' ':[5,6],'|':[0,1,2,3,4,7,8,9], '_':[]}
    return possibleNums[character]

def r3c1Func(character):
    possibleNums = {' ':[1,3,4,5,7,9],'|':[0,2,6,8], '_':[]}
    return possibleNums[character]

def r3c2Func(character):
    possibleNums = {' ':[1,4,7],'|':[], '_':[0,2,3,5,6,8,9]}
    return possibleNums[character]

def r3c3Func(character):
    possibleNums = {' ':[2],'|':[0,1,3,4,5,6,7,8,9], '_':[]}
    return possibleNums[character]


accountList = [] #List of Account objects
director = {'r1c2':r1c2Func, 'r2c1':r2c1Func, 'r2c2':r2c2Func, 'r2c3':r2c3Func, 'r3c2':r3c1Func, 'r3c2':r3c2Func, 'r3c3':r3c3Func,}
print(director['r1c2'](' '))

for item in director['r1c2'](' '):
    frameList[1]['p1'].iloc[item] = 1
#frameList[1]['p1'].iloc[0] = 1
print(frameList[1])
print(lines[0])
print(lines[0][4])
