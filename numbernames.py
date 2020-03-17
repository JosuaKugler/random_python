import codecs
import os

def readData():
    numberList = []
    with codecs.open('numbernames.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numberList.append(line)
    return numberList
numberList = readData()

def get_String(numberString,bigBlock):
    '''
    get String from an integer < 1000
    '''
    global numberList
    numberInt = int(numberString)
    if numberInt == 0:
        result = ''
    elif bigBlock == 1 and numberInt == 1:
        result = 'ein'
    elif bigBlock == 2 and numberInt == 1:
        return 'eine'
    else:
        result = numberList[numberInt-1][:-1]
    return result

def get_Latin_String(numberInt):
    global numberList
    if numberInt == 0:
        result = 'ni'
    else:
        result = numberList[numberInt+1000-1][:-1]
    return result

def latin_Translate(numberInt):
    integerString = str(numberInt)
    retString = ''
    while len(integerString) > 0:
        try:
            numbers = integerString[-3:]
            integerString = integerString[:-3]
        except:
            numbers = integerString
            integerString = ''
        blockString = get_Latin_String(int(numbers)) + "lli"
        retString = blockString + retString
    return retString


def get_blockString(blockNumber, numbers):
    '''
    get String from the blockNumberth block
    '''
    global numberList
    numbers = int(numbers)
    bigBlock = 2 #2: return eine, 1: return ein, 0: return eins
    if blockNumber == 0:
        bigBlock = 0
    elif blockNumber == 1:
        bigBlock = 1
    basicNumberString = get_String(numbers,bigBlock)

    if blockNumber == 0 or basicNumberString == '':
        blockString = ''

    elif blockNumber == 1:
        blockString = 'tausend'

    elif blockNumber < 2000 and numbers == 1:
        if blockNumber % 2 == 0:
            blockString = ' ' + numberList[1000+int(blockNumber/2)-1][:-1] + 'llion'
        else:
            blockString = ' ' + numberList[1000+int(blockNumber/2)-1][:-1] + 'lliarde'

    elif blockNumber < 2000 and numbers != 1:
        if blockNumber % 2 == 0:
            blockString = ' ' + numberList[1000+int(blockNumber/2)-1][:-1] + 'llionen'
        else:
            blockString = ' ' + numberList[1000+int(blockNumber/2)-1][:-1] + 'lliarden'

    elif numbers == 1:
        halfblocknumber = int(blockNumber/2)
        latinBlockName = latin_Translate(halfblocknumber)
        if blockNumber % 2 == 0:
            blockString = ' ' + latinBlockName + 'on'
        else:
            blockString = ' ' + latinBlockName + 'arde'

    else:
        halfblocknumber = int(blockNumber/2)
        latinBlockName = latin_Translate(halfblocknumber)
        if blockNumber % 2 == 0:
            blockString = ' ' + latinBlockName + 'onen'
        else:
            blockString = ' ' + latinBlockName + 'arden'

    #print('numbers:', numbers, 'blockNumber:', blockNumber, 'basicNumberString:', basicNumberString, 'blockString:', blockString)
    return str(basicNumberString) + str(blockString)


def translate(integer):
    integerString = str(integer)
    if int(integerString) == 0:
        return "null"
    retString = ''
    blocknumber = -1
    while len(integerString) > 0:
        blocknumber += 1
        try:
            numbers = integerString[-3:]
            integerString = integerString[:-3]
        except:
            numbers = integerString
            integerString = ''
        blockString = get_blockString(blocknumber, numbers)
        if blockString !='':
            retString = blockString + ' ' + retString

    return retString

#print(translate(input('zahl: ')))

print(translate(10**33330))
