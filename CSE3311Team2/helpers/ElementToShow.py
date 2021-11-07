from random import randint
import os
from ast import literal_eval

def getElementList(directory):
    elementList = []
    for files in os.listdir(directory):
        elementList.append(files.replace('.png',''))
    return elementList



def getElementName(directory):
    elementList = getElementList(directory)
    noOfElement= len(elementList)
#    threshold = 10000
#    randNo = 0
#    while True:
    randNo = (randint(0, noOfElement-1))
#        if elementList[randNo] in elementCount:
#            if elementCount[elementList[randNo]]<threshold:
#                break
#        else:
#            break

    return elementList[randNo]


def geTurktElementList(directory):
    elementList = []
    for files in os.listdir(directory):
        elementList.append(files.replace('.jpg',''))
    return elementList

def geTurktElementName(directory):
    elementList = geTurktElementList(directory)
    noOfElement= len(elementList)
#    threshold = 10000
#    randNo = 0
#    while True:
    randNo = (randint(0, noOfElement-1))
#        if elementList[randNo] in elementCount:
#            if elementCount[elementList[randNo]]<threshold:
#                break
#        else:
#            break

    return elementList[randNo]