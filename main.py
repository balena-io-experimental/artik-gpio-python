#!/usr/bin/python

from periphery import GPIO
import time

# pinNum = 135; for Artik 5
pinNum = 22;  #for Artik 10

LED = GPIO(pinNum, "out")

while True:
	LED.write(True)
	time.sleep(1)
	LED.write(False)
	time.sleep(1)
