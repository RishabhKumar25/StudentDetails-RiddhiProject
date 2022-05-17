import cv2
import numpy as np
import face_recognition
import os
import datetime
import pandas as pd

#import webbrowser

#webbrowser.open_new_tab('index  .html')

path='imageAttendance'
images=[]
classnames=[]
classUniqId=[]  #stores Unique Id
classname=[] #Stores name
myList= os.listdir(path)

for cls in myList:
    curImg=cv2.imread(f'{path}/{cls}')
    images.append(curImg)
    classnames.append(os.path.splitext(cls)[0])

for name in classnames:
    data= name.split(" ",1)
    classUniqId.append(data[0])  #separating id and name from photo name
    classname.append(data[1])


def markAttendance(name):
    with open('StudentAttendance.csv','r+') as f:
        myDataList=f.readlines()
        nameList=[]
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            nowd=datetime.datetime.now()
            dtStringY=nowd.strftime("%D %H:%M:%S")
            dtString = dtStringY.split(" ")
            f.writelines(f'\n{name},{dtString[0]},{dtString[1]}')


def getDetails(name):
    namei=int(name)
    file = pd.read_excel(io="StudentDetails.xlsx", sheet_name="Sheet1")
    dict = {2016900: [0, 'ABHAY TYAGI'], 2016901: [1, 'ABHIJOT KUMAR'], 2016902: [2, 'ABHINAV VERMA'],2016903: [3, 'ABHIRAM SINGH'],
            2016904: [4, 'ABHISHEK AWASTHI'], 2016905: [5, 'ABHYUDAY KUMAR'],2016906: [6, 'ADESH SENGER'], 2016907: [7, 'ADITI SINGH'],
            2016908: [8,'ADITYA DAYAL'], 2016909: [9,'AKASH GUPTA'],2016910: [10,'AMAN SINGH'], 2016911: [11,'AMULYA SRIVASTAVA'], 2016912: [12,'ANKIT SINGH'],
            2016913: [13,'ANUBHAV JOSHI'],2016914: [14,'ANUKRITI SINGH'], 2016915: [15,'ANUSHKA GHOSH'], 2016916: [16,'ANUSHKA MISHRA'], 2016917: [17,'APOORVA UNIYAL'],2016918: [18,'ARUSHI TIWARI'],
            2016919: [19,'ASHUTOSH VERMA'], 2016920:[20, 'BAISHALI DAS'], 2016921: [21,'CHIRAG AGARWAL'],2016922: [22,'CHIRAG TANDON'], 2016923:[23, 'DEVANSH BHATT'], 2016924: [24,'DIYA GOEL'],
            2016925: [25,'EKTA GUPTA'], 2016926: [26,'GAURAV RAI'], 2016927: [27,'HARSH GOEL'], 2016928: [28,'ISHA GUPTA'], 2016929: [29,'ISHIKA GARG'],2016930: [30,'JYOTI TUTEJA'],
            2016931: [31,'KABIR THAPAR'], 2016932:[32,'KOMAL SRIVASTAVA'], 2016933: [33,'KRAPI RASTOGI'],2016934: [34,'KUMAR EKLAVYA'], 2016935: [35,'KUMARI NEHA'], 2016936: [36,'KUSHAGRA SRIVASTAVA'],
            2016937: [37,'LAKSHYA SINGH'],2016938: [38,'MAMTA SHIVHARE'], 2016939: [39,'MANAN KAPOOR'], 2016940: [40,'MANMOHAN KISHORE'], 2016941: [41,'MANYA SINGH'],2016942: [42,'MAYANK SINGH'],
            2016943: [43,'MIHIKA SAXENA'], 2016944: [44,'MOHD. AZAM'], 2016945: [45,'NEEHARIKA DAS'],2016946: [46,'NEHIL BHATT'], 2016947: [47,'NIDHI VERMA'], 2016948: [48,'NAKSHTRA TYAGI'],
            2016949: [49,'OM SINGH'],2016950:[50, 'PRABHAV PANDE'], 2016951: [51,'PRANAV KAUSHAK'], 2016952: [52,'PRINCE PANDEY'], 2016953: [53,'PRIYA GUPTA'],2016954: [54,'PRIYA SAINI'],
            2016955: [55,'PRIYAL SRIVASTAVA'], 2016956: [56,'RAGHVEE SINGH'], 2016957: [57,'RAJVEER NEGI'],2016958: [58,'RASHI SONI'], 2016959: [59,'RASHMI GOEL'], 2016960: [60,'RIDDHI SHIVHARE'],
            2016961: [61,'RISHABH SRIVASTAVA'],2016962: [62,'RIYA MAHESHWARI'], 2016963: [63,'ROHIT BHARTI'], 2016964: [64,'ROSHAN SINGH'], 2016965: [65,'RUCHIKA SINGH'],
            2016966: [66,'SAHIL KUMAR'], 2016967: [67,'SAMEER MAHESHWARI'], 2016968: [68,'SAMPADA SINGH'], 2016969: [69,'SANYA DIKSHIT'],2016970: [70,'SATYAM KAPOOR'], 2016971: [71,'SHAILESH SINGH'],
            2016972: [72,'SHALEEN KAPOOR'],2016973:[73, 'SHIVAM SRIVASTAVA'], 2016974: [74,'SHIVANG SRIVASTAVA'], 2016975: [75,'SHRADDHA BAJPAI'],2016976: [76,'SHRAVAN BAJPAI'],
            2016977: [77,'SHREYA BAHUGUNA'], 2016978: [78,'SHRISHTI SINGH'], 2016979:[79, 'SHRUTI KANCHI'],2016980: [80,'SHUBHAM GUPTA'], 2016981: [81,'SHWETA VERMA'],
            2016982: [82,'SIDDHARTH VERMA'] ,2016983:[83, 'SIDDHI SHIVHARE'],2016984: [84,'SIMA SINGH'], 2016985: [85,'SMERA GOEL'], 2016986: [86,'SOHAM VAIDYA'],
            2016987: [87,'SONIKA GUPTA'],2016988: [88,'SRAJIT AGARWAL'], 2016989: [89,'SWARNA MATHPAL'], 2016990: [90,'TANYA GUPTA'], 2016991: [91,'TUHINA VERMA'],2016992: [92,'TUSHAR VERMA'],
            2016993: [93,'UJJWAL CHAUHAN'],2016994: [94,'UPENDRA SRIVASTAVA'], 2016995:[95, 'VAIBHAV SINGH'],2016996: [96,'VAISHNAVI BHATT'], 2016997: [97,'VIDHUSHI SINGH'],
            2016998: [98,'VIRAJ NAIR'],2016999:[ 99,'VIVEK SAHAY']}
    print(file.iloc[dict[namei][0]])

#creating the encoding list
encodeListKnown=[]
with open("encoding.txt", "r") as f:
     #lines=f.readline()
     while True:
      lines = f.readline()
      if(lines==''):
         break
      encode=[]
      encode.append(float(lines))
      for i in range(127):
         lines = f.readline()
         encode.append(float(lines))
      encodeListKnown.append(encode)



cap=cv2.VideoCapture(0)

while True:
    success , img = cap.read()
    imgS =cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurr = face_recognition.face_locations(imgS)
    encodeCurr = face_recognition.face_encodings(imgS,faceCurr)

    for enf,floc in zip(encodeCurr,faceCurr):
        matches=face_recognition.compare_faces(encodeListKnown,enf)
        faceDis=face_recognition.face_distance(encodeListKnown,enf)
        #print(faceDis)
        matchIndex=np.argmin(faceDis)
        min =np.amin(faceDis)
        #print(min)

        #print(matchIndex)
        if matches[matchIndex]:
            id= classUniqId[matchIndex].upper()
            name = classname[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1=floc
            y1, x2, y2, x1 =y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(145,60,255),2)
            #cv2.rectangle(img,(x1, y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            #cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            #print(min)
            if (min < 0.4000000):
              markAttendance(name)
              getDetails(id)
            else:
              print("Record not found")
    cv2.imshow('webcam',img)
    #cv2.waitKey(0)
    if cv2.waitKey(0) & 0xFF == ord(' '):
        break
#cv2.destroyAllWindows()
print("DONE")

    #cv2.imshow('webcam', img)
    #if cv2.waitKey(0): #& 0xFF ==ord(' '):
     #   break
#cv2.destroyAllWindows()
