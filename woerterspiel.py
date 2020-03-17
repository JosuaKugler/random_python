import codecs
import os

def simplifylist(liste):
    retlist=[]
    elementinlist=[]
    for element in liste:
        if element not in elementinlist:
            elementinlist.append(element)
            retlist.append(element)
    return retlist

def copy(liste):
    liste2=[]
    for i in liste:
        liste2.append(i)
    return liste2

def anagramm(word1,wordlist):
    """
    Input:  Zwei Wörter
    Output: True  wenn die mittleren Buchstaben der beiden Wörter ein Anagramm bilden
            False ansonsten
    """
    wordlist1=list(word1)
    for i in wordlist1:
        if i in wordlist:
            wordlist.remove(i)
        else:
            return False
    if len(wordlist)>0:
        return False
    return True
with codecs.open("woerterliste.txt","r",encoding="utf-8") as f:
    woerterliste=[line.rstrip('\n') for line in f]

sorteddict={}
for word in woerterliste:
    word = word[0].lower()+word[1:]
    len1 = len(word)
    try:
        a = sorteddict[len1]
    except:
        sorteddict[len1] = []
    sorteddict[len1].append(word)


def findwords(wordlist,length):
    retlist=[]
    if len(wordlist)<length:
        return retlist
    elif len(wordlist)>length:
        for i in wordlist:
            wordlist2 = copy(wordlist)
            wordlist2.remove(i)
            liste = findwords(wordlist2,length)
            for i in liste:
                retlist.append(i)
        return retlist
    else:
        for word in sorteddict[length]:
            if anagramm(word, copy(wordlist)):
                retlist.append(word)
        return retlist

def findallwords(wordlist):
    for i in range(2,len(wordlist)+1):
        print(i,":",simplifylist(findwords(wordlist,i)))

findallwords(list(input()))
