import speech_recognition as s
sr= s.Recognizer()
print("im listenning to you............")
with s.Microphone() as m:
    audio= sr.listen(m)
    query=sr.recognize_google(audio,language="en-us")
    print(query)
    
    
import pyttsx3                         #this code here will speak out your said voice command
engine = pyttsx3.init()
engine.say(query)
engine.runAndWait()


  
  

