#!/usr/bin/env python3
import os
import Adafruit_BBIO.GPIO as GPIO
import smbus
import time

bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

# Specifies the start position for the cursor the leftmost 2 columns and the  
# top row are reserved to give the grid numbers to make it more visually 
# appealing
current_width = 0
current_height = 0

# setup for input pins, which are wired to pushbuttons
PB1 = "P8_7"
PB2 = "P8_9"
PB3 = "P8_15"
PB4 = "P8_17"
GPIO.setup(PB1, GPIO.IN)
GPIO.setup(PB2, GPIO.IN)
GPIO.setup(PB3, GPIO.IN)
GPIO.setup(PB4, GPIO.IN)

# function allowing the first pushbutton to move the cursor up
def callback1(channel):
    global current_height
    global current_width
    if(current_height > 0):
        current_height-= 1
        array[current_height][current_width] = "X"
        update_output()
    
# function allowing the second pushbutton to move the cursor down
def callback2(channel):
    global current_height
    global current_width
    if(current_height < (size - 1)):
        current_height+= 1
        array[current_height][current_width] = "X"
        update_output()

# function allowing the third pushbutton to move the cursor left
def callback3(channel):
    global current_height
    global current_width
    if(current_width > 0):
        current_width -= 1
        array[current_height][current_width] = "X"
        update_output()
    
# function allowing the fourth pushbutton to move the cursor right
def callback4(channel):
    global current_height
    global current_width
    if(current_width < (size - 1)):
        current_width += 1
        array[current_height][current_width] = "X"
        update_output()
    
def update_output():
	# clears the screen, then uses nested for loops to print the array
    for l in range(size):
        curSum = 0
        for k in range(size):
            if(array[k][l] == "X"):
                curSum+=2**k
        ledVals[2*(l+1) - 1] = curSum
        ledVals[2*l] = 0
    ledVals[2*current_width] = 2**current_height
    bus.write_i2c_block_data(matrix, 0, ledVals)
		
def clear_etcher():
	# Uses nested for loops to empty the array, 
	for row in range(0, size):
		for col in range(0, size):
			array[row][col] = " "
	update_output()

size = 8
array = [[" " for i in range (size)] for j in range(size)]
ledVals = [0 for i in range (size *2)]

# setup for event detection done in the loop
array[current_height][current_width] = "X"
update_output()

GPIO.add_event_detect(PB1, GPIO.RISING, callback=callback1)
GPIO.add_event_detect(PB2, GPIO.RISING, callback=callback2)
GPIO.add_event_detect(PB3, GPIO.RISING, callback=callback4)
GPIO.add_event_detect(PB4, GPIO.RISING, callback=callback3)


# Loop to read keyboard input and update the display of the grid on the console
while(1):
	dir = input("Press pushbuttons to move the Etch-A-Sketch! (or Spacebar to clear)")
	if(dir == " "):
		clear_etcher()
	array[current_height][current_width] = "X"
	update_output()