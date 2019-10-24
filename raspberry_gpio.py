#!/usr/bin/python3
#encoding:utf-8


import RPi.GPIO as GPIO

led=26
man_sensor=19

GPIO.setmode(GPIO.BCM)

GPIO.setup(led,GPIO.OUT)
GPIO.setup(man_sensor,GPIO.IN)

try:
    while True:
        if(GPIO.input(man_sensor)==True):
            GPIO.output(led,True)
            print("led bright!")
        else:
            GPIO.output(led,False)
            print("led off!")
except keyboardInterrupt:
    pass

GPIO.cleanup()



