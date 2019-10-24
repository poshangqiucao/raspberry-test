#!/usr/bin/python3
#encoding:utf-8

import RPi.GPIO as GPIO
import time

led = 26
trig1 = 19
echo1 = 13
trig2 = 21
echo2 = 20
trig3 = 17
echo3 = 27

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(led,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(trig1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(trig2,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(trig3,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(echo1,GPIO.IN)
GPIO.setup(echo2,GPIO.IN)
GPIO.setup(echo3,GPIO.IN)

def get_distance(trig,echo):
    GPIO.output(trig,GPIO.HIGH)
    time.sleep(0.000012)
    GPIO.output(trig,GPIO.LOW)
    while not GPIO.input(echo):
        pass
    t1 = time.time()
    while GPIO.input(echo):
        pass
    t2 = time.time()
    return (t2-t1)*340/2

while True:
    time.sleep(0.5)
    if get_distance(trig1,echo1)*100 < 15 or get_distance(trig2,echo2)*100 <15 or get_distance(trig3,echo3)*100 <15:
        GPIO.output(led,GPIO.HIGH)
    else:
        GPIO.output(led,GPIO.LOW)
    print(get_distance(trig1,echo1)*100,get_distance(trig2,echo2)*100,get_distance(trig3,echo3)*100)









