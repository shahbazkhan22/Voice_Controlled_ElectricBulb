# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 22:50:46 2017

@author: shahb
"""

                                                                                                      
import speech_recognition as sr  
import serial
# Opening the serial port 'COM9' with baudrate set to 9600    
port = serial.Serial('COM9', 9600 , timeout=0)                                                                   
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:
    x=input('Do you want to continue?(y/n)')
    #print(x)
    #port.write('1'.encode())
    if(x=='y'):                                                                       
        print("Speak:") 
        #print("Hello")                                                                                  
        audio = r.listen(source)
        #print("Hello")
        print("Speech recorded")
        inSound = r.recognize_google(audio)
        print (inSound)
        if(inSound=='switch on'):
            inSound = '0'
        else:
             inSound = '1'   
        port.write(inSound.encode())
        if inSound == "break":
            break
    else:
        break
#try:
#    print(r.recognize_google(audio))
#except sr.UnknownValueError:
#   print("Could not understand audio")
#except sr.RequestError as e:
#    print("Could not request results; {0}".format(e))
