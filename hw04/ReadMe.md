## What's here? 
This directory contains a multitude of different scripts and visual files. Code
that is runnable includes mmapGPIO.py and mmapGPIOFast.py, which address the mmap
portion of the homework. To read the TMP101 sensors using the kernel driver, use
kernelI2C.sh . Additionally, the newest iteration of the Etch-A-Sketch game is 
named flaskEtch.py and allows browser control of the LED matrix. The last script
is text.sh, which is run to display text to the LCD. 

Additional files included here are the templates folder, boris.jpg, hst_1.mpg, 
and RedsNightmare.mpg. Their uses will be explained later. 

## mmapGPIO.py and mmapGPIOFast.py
Running mmapGPIO.py allows the user to toggle 2 LED light using a pushbutton. 
Contrary to previous times we have done this, here it is done using mmap for the
LED setup and inversion.

The other program, mmapGPIOFast.py, toggles an LED as quickly as possible using
mmap. This time, no button is necessary. The speed was about 90kHz.

Both files are run using python3 at the terminal. 

## kernelI2C.sh
This file, which is run at the terminal, reads the I2C bus using kernel drivers. 
Doing so outputs the temperature values being picked up by the TMP101 sensors.

## flaskEtch.py
This is a python file that is run to allow the user to change the LED matrix via 
a browser. Doing so requires the use of index.html in the templates folder, which
is used to generate the webpage that provides user input. After the user runs 
flaskEtch.py in the terminal using python3. Then, the user must direct their 
browser to 192.168.7.2, where they will see a webpage that provides buttons for
UP, DOWN, LEFT, RIGHT, and CLEAR. Clicking them manipulates the LED matrix as 
one would expect. 

## text.sh
This is a simple file that one can run in the terminal to display text on 
the LCD screen. It works using a blank blue background as an image, but 
works similarly for other images. 

## Other files
The other files are displayed via terminal commands. To display boris.jpg:

sudo fbi -noverbose -T 1 -a boris.jpg

and to display RedsNightmare.mpg:

mplayer -vo fbdev2 -nolirc -framedrop RedsNightmare.mpg