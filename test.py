from sklearn.neighbors import KNeighborsClassifier
import cv2
import pickle
import numpy as np
import os
import csv
import time
import pyttsx3
from datetime import datetime
from deepface import DeepFace

# Set up text-to-speech engine
engine = pyttsx3.init()

from win32com.client import Dispatch

def speak(str1): 
    speak=Dispatch(("SAPI.SpVoice"))
    speak.Speak(str1)

video=cv2.VideoCapture(0)
facedetect=cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

with open('data/names.pkl', 'rb') as f:
    LABELS=pickle.load(f)
with open('data/faces_data.pkl', 'rb') as f:
    FACES=pickle.load(f)

print('Shape of Faces matrix --> ', FACES.shape)

knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)

# imgBackground=cv2.imread("background.png")

COL_NAMES = ['NAME', 'TIME']

while True:
    ret,frame=video.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=facedetect.detectMultiScale(gray, 1.3 ,5)
    for (x,y,w,h) in faces:
        crop_img=frame[y:y+h, x:x+w, :]
        resized_img=cv2.resize(crop_img, (50,50)).flatten().reshape(1,-1)
        output=knn.predict(resized_img)
        ts=time.time()
        date=datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
        timestamp=datetime.fromtimestamp(ts).strftime("%H:%M-%S")
        exist=os.path.isfile("Attendance/Attendance_" + date + ".csv")
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),2)
        cv2.rectangle(frame,(x,y-40),(x+w,y),(50,50,255),-1)
        cv2.putText(frame, str(output[0]), (x,y-15), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (50,50,255), 1)
        attendance=[str(output[0]), str(timestamp)]
    # imgBackground[162:162 + 480, 55:55 + 640] = frame
    cv2.imshow("Frame",frame) #imgBackground
    k=cv2.waitKey(1)
    if k==ord('o'):
        speak("Attendance Taken..")
        time.sleep(5)
        if exist:
            with open("Attendance/Attendance_" + date + ".csv", "+a") as csvfile:
                writer=csv.writer(csvfile)
                writer.writerow(attendance)
            csvfile.close()
        else:
            with open("Attendance/Attendance_" + date + ".csv", "+a") as csvfile:
                writer=csv.writer(csvfile)
                writer.writerow(COL_NAMES)
                writer.writerow(attendance)
            csvfile.close()
    if k==ord('q'):
        break

    # Speak the name of the person
    engine.say(f"Hi {output}")
    engine.runAndWait()

    # Analyze mood using DeepFace
    try:
        analysis = DeepFace.analyze(frame, actions=['emotion'])
        mood = analysis[0]['dominant_emotion']
        print(f"Mood detected: {mood}")
            
        # Provide feedback based on the mood
        if mood == 'happy':
            engine.say(f"Hi {output}, your mood today is happy! Keep up the positive energy!")
        elif mood == 'sad':
            engine.say(f"Hi {output}, your mood today is sad. Stay strong and positive!")
        elif mood == 'angry':
            engine.say(f"Hi {output}, your mood today is angry. Take a deep breath and relax.")
        else:
            engine.say(f"Hi {output}, your mood is {mood}. Stay positive!")
        engine.runAndWait()
    except Exception as e:
        print("Error analyzing mood:", e)

video.release()
cv2.destroyAllWindows()

