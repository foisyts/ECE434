## What's here? 
Both of the TMP101 files (one using the shell and one using python) can be 
found in the tempSensor.sh and tempSensor.py files, respectively. Both output 
in Farenheit. The file hw03.py is the updated Etch-a-sketch game, this time
using the LED light array. 

## tempSensor.sh and tempSensor.py
These two files are grouped together because they are both simple scripts, which 
makes them very similar to one another. Both read from the i2c bus via pins 19 
and 20. After receiving a value, they convert it to Farenheit and print it to 
the console. The .sh file uses i2cget to handle i2c communication while the .py
file does so using the smbus package. 

## hw03 
This file is the third iteration of the Etch-a-sketch game, this time featuring 
a physical 8x8 LED matrix. Like before, it can be controlled by using the 
leftmost button to move the  cursor up, second from the left to move the cursor
down, second from the  right to move the cursor left, and rightmost button is 
to move the cursor right. Also like before, spacebar can be used to clear the 
LED matrix. 

One noteworthy feature is how the current position is shown in a different color 
than previously visited squares. This helps the user to keep track of where the
cursor is even when backtracking. 

This implementation of the LED matrix is interesting as it translates the 2D 
matrix used previously into the binary input used by the LED i2c. The math 
involved uses nested for loops to track column info, which is used to use powers
of 2 to get the correct value as the cursor moves across the screen. 

# hw03 grading

| Points      | Description |
| ----------- | ----------- |
|  5/5 | TMP101 
|  3/3 |   | setup.sh
|  2/2 |   | Documentation 
|  0/5 | Etch-a-Sketch | Not Demo'ed - Demo for more credit
|  3/3 |   | setup.sh
|  2/2 |   | Documentation
| 15/20 | **Total**