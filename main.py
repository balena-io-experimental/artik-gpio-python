#!/usr/bin/python

import RPi.GPIO as GPIO
import time

# Set GPIO mode: GPIO.BCM or GPIO.BOARD
GPIO.setmode(GPIO.BOARD)

# pinNum = 135; for Artik 5
pinNum = 22;  #for Artik 10

GPIO.setup(pinNum, GPIO.OUT)

while True:
	GPIO.output(pinNum, True)
	time.sleep(1)
	GPIO.output(pinNum, False)
	time.sleep(1)
