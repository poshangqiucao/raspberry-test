#!/usr/bin/python3
#encoding:utf-8

import RPi.GPIO as GPIO
import time

led = 26
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(led,GPIO.LOW)
pwm = GPIO.PWM(led,60)
pwm.start(0)
while True:
    #for dc in range(0,101,10):
     #   pwm.ChangeDutyCycle(dc)
      #  time.sleep(0.7)
    #for dc in range(100,0,-10):
     #   pwm.ChangeDutyCycle(dc)
      #  time.sleep(0.2)
    pwm.ChangeDutyCycle(70)
#GPIO.output(led,GPIO.HIGH)


