import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import csv
from itertools import compress

def findTrainingEncodings(StudentImages):
    encodeList = []
    for img in StudentImages:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]    #Training images has only one face
        encodeList.append(encode)
    return encodeList

def findLoc(StudentImages):
    for img in StudentImages:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        faceLoc = face_recognition.face_locations(img)[0]
        cv2.rectangle(img, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)
        print(faceLoc)

def findTestEncodings(StudentUplaodedImages):
    encodeList1 = []
    for img1 in StudentUplaodedImages:
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        locs = face_recognition.face_locations(img1)    #Test img should use all the locations
        for i in range(len(locs)):
            encode1 = face_recognition.face_encodings(img1)[i]
            encodeList1.append(encode1)
    return encodeList1

def findLoc1(StudentUplaodedImages):
    for img1 in StudentUplaodedImages:
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        return face_recognition.face_locations(img1)[0]
        cv2.rectangle(img1, (faceLoc1[3], faceLoc1[0]), (faceLoc1[1], faceLoc1[2]), (255, 0, 255), 2)
        print(faceLoc1)

def calculateMatchPercent(loc):
    m = loc*2
    if m <= 1:
        return 100
    elif m > 1 and m <= 1.1:
        return 80
    elif m > 1.1 and m <= 1.3:
        return 70
    elif m > 1.3 and m <= 1.5:
        return 60
    elif m > 1.5 and m <= 1.7:
        return 50
    elif m > 1.7 and m <= 1.9:
        return 40
    elif m > 1.9 and m <= 2.1:
        return 30
    elif m > 2.1 and m <= 2.3:
        return 30
    elif m > 2.3 and m <= 2.5:
        return 20
    elif m > 2.5:
        return 10

def Run():
    path = 'rollcallmodule/StudentImages'
    StudentImages = []
    classNames = []
    myList = os.listdir(path)
    print(myList)

    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        StudentImages.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)

    encodeListKnown = findTrainingEncodings(StudentImages)
    print(len(encodeListKnown))
    print('Encoding Complete')

    path = 'rollcallmodule/StudentUplaodedImages'
    StudentUplaodedImages = []
    classNames1 = []
    myList1 = os.listdir(path)
    print(myList1)

    for cl1 in myList1:
        curImg = cv2.imread(f'{path}/{cl1}')
        StudentUplaodedImages.append(curImg)
        classNames1.append(os.path.splitext(cl1)[0])
    print(classNames1)

    encodeListUnknown = findTestEncodings(StudentUplaodedImages)
    print(len(encodeListUnknown))
    print('Encoding Complete')

    LocList1 = findLoc1(StudentUplaodedImages)
    print(LocList1)
    print(len(LocList1))

    matchedStudents = []
    myDict={}
    for encUnknown in encodeListUnknown:
        result = face_recognition.compare_faces(encodeListKnown, encUnknown)
        faceDis = face_recognition.face_distance(encodeListKnown, encUnknown)
        print("Given match list is : " + str(result))
        print("Face Distance is", faceDis)
        res = list(compress(range(len(result)), result))
        print("Indices having True values are : " + str(res))
        matchIndex = np.argmin(faceDis)
        if True in result:
            print("The uploaded file was matched with the existing photos")
        else:
            print("Not photos matched")
        if result[matchIndex]:
            name = classNames[matchIndex].upper()
            matchedStudents.append(name)
            print("Matched photo ID is:", name)
            myDict[name] = calculateMatchPercent(faceDis[matchIndex])

    print("Matched Id's: ", matchedStudents)
    print(myDict)
    return myDict

