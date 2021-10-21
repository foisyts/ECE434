#!/usr/bin/python3

from mmap import mmap
import time
import struct
import Adafruit_BBIO.GPIO as GPIO 

# setup  for GPIO 
GPIO1_offset = 0x4804c000
GPIO1_size = 0x4804cfff-GPIO1_offset
GPIO_OE = 0x134
GPIO_SETDATAOUT = 0x194
GPIO_CLEARDATAOUT = 0x190

# locations of LEDs and Pushbuttons
LEDGreen = 1<<27
LEDRed = 1<<18
PB1 = "P8_7"
PB2 = "P8_9"

# Setup for GPIO on pushbuttons
GPIO.setup(PB1, GPIO.IN)
GPIO.setup(PB2, GPIO.IN)
GPIO.add_event_detect(PB1, GPIO.RISING)
GPIO.add_event_detect(PB2, GPIO.RISING)

# initialiazation to use mmap for GPIO handling
with open("/dev/mem", "r+b") as f:
    mem = mmap(f.fileno(), GPIO1_size, offset=GPIO1_offset)
    
packed_reg=mem[GPIO_OE:GPIO_OE+4]
reg_status = struct.unpack("<L", packed_reg)[0]
reg_status &= ~(LEDRed)
reg_status &= ~(LEDGreen)
mem[GPIO_OE:GPIO_OE+4] = struct.pack("<L", reg_status)
pb1_status = 0
pb2_status = 0

# listen for changes in the pushbutton - if heard, invert value of the LED by changing packed 
# value in memory. 
while(True):
    if(GPIO.event_detected(PB1)):
        if(pb1_status == 0):
            mem[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", LEDGreen)
            pb1_status = 1
        else:
            mem[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", LEDGreen)
            pb1_status = 0
    if(GPIO.event_detected(PB2)):
        if(pb2_status == 0):
            mem[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", LEDRed)
            pb2_status = 1
        else:
            mem[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", LEDRed)
            pb2_status = 0
            
