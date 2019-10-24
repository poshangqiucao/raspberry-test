#!/usr/bin/python3
#encoding:utf-8

import RPi.GPIO as GPIO
import time

data=[]
j=0
dht11_pin = 6


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
time.sleep(1)

GPIO.setup(dht11_pin,GPIO.OUT)
GPIO.output(dht11_pin,GPIO.LOW)
time.sleep(0.02)
GPIO.output(dht11_pin,GPIO.HIGH)

GPIO.setup(dht11_pin,GPIO.IN)

while GPIO.input(dht11_pin)==GPIO.LOW:
    continue

while GPIO.input(dht11_pin)==GPIO.HIGH:
    continue

while j<40:
    k=0
    while GPIO.input(dht11_pin)==GPIO.LOW:
        continue
    while GPIO.input(dht11_pin)==GPIO.HIGH:
        k+=1
        if k>100:
            break
    if k<8:
        data.append(0)
    else:
        data.append(1)
    j+=1


print("传感器正在工作...")
print(data)

humidity_bit = data[0:8]
humidity_point_bit = data[8:16]
temperature_bit = data[16:24]
temperature_point_bit = data[24:32]
check_bit = data[32:40]

humidity = 0
humidity_point = 0
temperature = 0
temperature_point = 0
check = 0

for i in range(8):
    humidity += humidity_bit[i]*2**(7-i)
    humidity_point += humidity_point_bit[i]*2**(7-i)
    temperature += temperature_bit[i]*2**(7-i)
    temperature_point += temperature_point_bit[i]*2**(7-i)
    check += check_bit[i]*2**(7-i)
    
tem = humidity+humidity_point+temperature+temperature_point

if tem==check:
    print("湿度：",humidity,".",humidity_point," 温度：",temperature,".",temperature_point)
else:
    print("数据错误！")

GPIO.cleanup()





