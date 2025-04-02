#Date: 31/3/2025
#Auther: Yang Yue
#Student NUIST ID: 202283890018 
#Student SETU ID: W20109667


import RPi.GPIO as GPIO    #using RPi.GPIO library
import time                #using time library

GPIO.setmode(GPIO.BCM)     #tell the name of pins
GPIO.setwarnings(False)    
GPIO.setup(18,GPIO.OUT)    
print("LED on")            #print this message to the terminal
GPIO.output(18,GPIO.HIGH)  #turn the 'GPIO' pin 'on'
time.sleep(1)              #pause the program for 1 second
print("LED off")           #print this message to the terminal
GPIO.output(18,GPIO.LOW)   #turn the 'GPIO' pin 'off'

