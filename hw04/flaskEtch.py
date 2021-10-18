#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import smbus
import time
from flask import Flask, render_template, request
app = Flask(__name__)

bus = smbus.SMBus(2)  # Use i2c bus 2
matrix = 0x70         # Use address 0x70 for LED array

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

# Specifies the start position for the cursor in the top right corner of the LED 
# array
current_width = 0
current_height = 0
    
def update_output():
	# maps the 2D array to the LED array, which is done by calculating binary 
    # value and sending them to the i2c bus (nested loop implementation)
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
	# Uses nested for loops to empty the 2D array 
	for row in range(0, size):
		for col in range(0, size):
			array[row][col] = " "
	update_output()

# Setup for 8x8 matrix size, including 8x8 2D array to store visited squares 
# and 1D array to store binary values for LED array
size = 8
array = [[" " for i in range (size)] for j in range(size)]
ledVals = [0 for i in range (size *2)]

# setup for event detection done in the loop
array[current_height][current_width] = "X"
update_output()

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    global current_height, current_width, array
    if action == "down":
        if(current_height < (size - 1)):
            current_height+= 1
            array[current_height][current_width] = "X"
            update_output()
    if action == "up":
        if(current_height > 0):
            current_height-= 1
            array[current_height][current_width] = "X"
            update_output()
    if action == "left":
        if(current_width > 0):
            current_width -= 1
            array[current_height][current_width] = "X"
            update_output()
    if action == "right":
        if(current_width < (size - 1)):
            current_width += 1
            array[current_height][current_width] = "X"
            update_output()
    if action == "clear":
        clear_etcher()
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(port=8081, host='0.0.0.0', debug=True)