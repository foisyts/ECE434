#!/usr/bin/env python3
import os
import Adafruit_BBIO.GPIO as GPIO

# Specifies the start position for the cursor the leftmost 2 columns and the  
# top row are reserved to give the grid numbers to make it more visually 
# appealing
current_width = 2
current_height = 1

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
    if(current_height > 1):
        current_height-= 1
        array[current_height][current_width] = "X"
        update_output()
    
# function allowing the second pushbutton to move the cursor down
def callback2(channel):
    global current_height
    global current_width
    if(current_height < (size)):
        current_height+= 1
        array[current_height][current_width] = "X"
        update_output()

# function allowing the third pushbutton to move the cursor left
def callback3(channel):
    global current_height
    global current_width
    if(current_width > 2):
        current_width -= 1
        array[current_height][current_width] = "X"
        update_output()
    
# function allowing the fourth pushbutton to move the cursor right
def callback4(channel):
    global current_height
    global current_width
    if(current_width < (size+1)):
        current_width += 1
        array[current_height][current_width] = "X"
        update_output()
    
def update_output():
	# clears the screen, then uses nested for loops to print the array
	os.system('cls' if os.name == 'nt' else 'clear')
	for k in range(size+1):
		for l in range(size+2):
			print(array[k][l], end = '')
		print("")
		
def clear_etcher():
	# Uses nested for loops to empty the array, 
	for row in range(1, size+1):
		for col in range(2, size+2):
			array[row][col] = " "

size = input("Enter the size of square matrix (number key): ")
size = int(size)
array = [[" " for i in range (size + 2)] for j in range(size +1)]


print("\n")
# Additional setup for the grid: this puts index numbers on the top and left 
# sides, then places the cursor onto the grid
for height in range(0,size+1):
	for width in range(0, size+2):
		# Top row - index numbers
		if height == 0 :
			if ((width != 0) and (width != 1)):
				array[height][width] = width - 2
		# leftmost column - index numbers
		elif width == 0:
			array[height][width] = height - 1
		# second leftmost column - colons 
		elif width == 1:
			array[height][width] = ":"
		# placing the cursor
		elif width == 2:
			if height == 1:
				array[current_height][current_width] = "X"
				
update_output()

# setup for event detection done in the loop
GPIO.add_event_detect(PB1, GPIO.RISING, callback=callback1)
GPIO.add_event_detect(PB2, GPIO.RISING, callback=callback2)
GPIO.add_event_detect(PB3, GPIO.RISING, callback=callback3)
GPIO.add_event_detect(PB4, GPIO.RISING, callback=callback4)

# Loop to read keyboard input and update the display of the grid on the console
while(1):
	dir = input("Press pushbuttons to move the Etch-A-Sketch! (or Spacebar to clear)")
	if(dir == " "):
		clear_etcher()
	array[current_height][current_width] = "X"
	update_output()