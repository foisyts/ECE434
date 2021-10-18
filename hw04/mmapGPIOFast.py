#!/usr/bin/python3

from mmap import mmap
import time
import struct
import Adafruit_BBIO.GPIO as GPIO 

GPIO1_offset = 0x4804c000
GPIO1_size = 0x4804cfff-GPIO1_offset
GPIO_OE = 0x134
GPIO_SETDATAOUT = 0x194
GPIO_CLEARDATAOUT = 0x190

LEDGreen = 1<<27
LEDRed = 1<<18

with open("/dev/mem", "r+b") as f:
    mem = mmap(f.fileno(), GPIO1_size, offset=GPIO1_offset)
    
packed_reg=mem[GPIO_OE:GPIO_OE+4]
reg_status = struct.unpack("<L", packed_reg)[0]
reg_status &= ~(LEDRed)
reg_status &= ~(LEDGreen)
mem[GPIO_OE:GPIO_OE+4] = struct.pack("<L", reg_status)

while(True):
    mem[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", LEDGreen)
    mem[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", LEDRed)
    mem[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", LEDGreen)
    mem[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", LEDRed)

   
            
