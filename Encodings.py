import cv2
import face_recognition
import os


images=[]
classnames=[]

path='imageAttendance'
myList=os.listdir(path)
for cls in myList:
    curImg=cv2.imread(f'{path}/{cls}')
    images.append(curImg)
    classnames.append(os.path.splitext(cls)[0])




def findencodings(images):
    encodeList=[]
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown=findencodings(images)
#encodeListKnown is a list of lists
print(len(encodeListKnown))

#writing the list value (encodeListKnown) in a text file
with open("encoding.txt", "w") as f:
    for i in encodeListKnown:
         for k in i:
             f.write(str(k)+"\n")

         #f.write('\n')

