import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 
GPIO.setup(17,GPIO.OUT) 

def morse(x):
  if (x == 'a'):
    GPIO.output(17,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(17,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(17,GPIO.HIGH)
    time.sleep(1)
    
  elif (x == 'e'):
    GPIO.output(17,GPIO.HIGH)
    time.sleep(0.5)
  
  elif (x == 'i'):
    GPIO.output(17,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(17,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(17,GPIO.HIGH)
    time.sleep(0.5)
    
  elif (x == 'k'):
    GPIO.output(17,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(17,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(17,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(17,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(17,GPIO.HIGH)
    time.sleep(1)
    
  elif (x == 'm'):
    GPIO.output(17,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(17,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(17,GPIO.HIGH)
    time.sleep(1)
    
  elif (x == 'n'):
    GPIO.output(17,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(17,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(17,GPIO.HIGH)
    time.sleep(0.5)
  
  elif (x == 'r'):
    GPIO.output(17,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(17,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(17,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(17,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(17,GPIO.HIGH)
    time.sleep(0.5)
    
  elif (x == 'u'):
    GPIO.output(17,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(17,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(17,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(17,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(17,GPIO.HIGH)
    time.sleep(1)
    
  elif (x == 'v'):
    GPIO.output(17,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(17,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(17,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(17,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(17,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(17,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(17,GPIO.HIGH)
    time.sleep(1)
    
  else :
    GPIO.output(17,GPIO.LOW)
    time.sleep(2)
    
 GPIO.output(17,GPIO.LOW)
 time.sleep(1)
 
s = "enikku urakkam varanu"
msg = [*s]

for i in msg:
  morse(msg[i])
 
