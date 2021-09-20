#! /usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO

# Defining pin locations for the pushbuttons and LEDs
PB1 = "P8_7"
PB2 = "P8_9"
PB3 = "P8_15"
PB4 = "P8_17"
LED1 =  "P8_8"
LED2 =  "P8_10"
LED3 = "P8_16"
LED4 =  "P8_18"

# pin setupus for the inputs(pushbuttons) and outputs (LEDs)
GPIO.setup(PB1, GPIO.IN)
GPIO.setup(PB2, GPIO.IN)
GPIO.setup(PB3, GPIO.IN)
GPIO.setup(PB4, GPIO.IN)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)

bool1 = False
bool2 = False
bool3 = False
bool4 = False

# inverts the current state of the first LED
def callback1(channel):
    global bool1
    bool1 = (not bool1)
    if(bool1):
        GPIO.output(LED1, GPIO.HIGH)
    else:
        GPIO.output(LED1, GPIO.LOW)

# inverts the current state of the second LED
def callback3(channel):
    global bool2
    bool2 = (not bool2)
    if(bool2):
        GPIO.output(LED2, GPIO.HIGH)
    else:
        GPIO.output(LED2, GPIO.LOW)
    
# inverts the current state of the third LED
def callback5(channel):
    global bool3
    bool3 = (not bool3)
    if(bool3):
        GPIO.output(LED3, GPIO.HIGH)
    else:
        GPIO.output(LED3, GPIO.LOW)

# inverts the current state of the fourth LED
def callback7(channel):
    global bool4
    bool4 = (not bool4)
    if(bool4):
        GPIO.output(LED4, GPIO.HIGH)
    else:
        GPIO.output(LED4, GPIO.LOW)
    

GPIO.add_event_detect(PB1, GPIO.RISING, callback=callback1)
# GPIO.add_event_detect(PB1, GPIO.FALLING, callback = callback2) Deprecated attempt to use falling edge & rising edge
GPIO.add_event_detect(PB2, GPIO.RISING, callback=callback3)
# GPIO.add_event_detect(PB2, GPIO.FALLING, callback = callback4)Deprecated attempt to use falling edge & rising edge
GPIO.add_event_detect(PB3, GPIO.RISING, callback=callback5)
# GPIO.add_event_detect(PB3, GPIO.FALLING, callback = callback6)Deprecated attempt to use falling edge & rising edge
GPIO.add_event_detect(PB4, GPIO.RISING, callback=callback7)
# GPIO.add_event_detect(PB4, GPIO.FALLING, callback = callback8)Deprecated attempt to use falling edge & rising edge
    
# loop to keep the program alive
while(1):
    if(1==2):
        print("wow")