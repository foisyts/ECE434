## What's here?
The results from the oscilloscope portion can be found in the oscilloscope.txt file,
while buttonPress.py can be used to turn on/off 4 LEDs. hw02.py is the updated Etch-
a-Sketch file. 

## oscilloscope.txt
Answered here are the 11 questions outlined in the homeworkd document.

## buttonPress.py
This program is used to toggle 1 of 4 LEDs on and off. After running it in the 
console, one needs only to push 1 of the 4 pushbuttons to toggle an LED. Each button
is mapped to its own LED. 

It was implemented by setting up 8 GPIO pins (4 inputs, 4 outputs) and then creating
a callback function that inverted a boolean whenever the corresponding button is 
pressed. When the boolean is true, the light is on.

## hw02.py
This is the revised Etch-a-sketch program! To start it, it needs to be launched from
the console while in the directory where it resides. After that, it prompts the user
for the size of the input matrix that will be used. Pressing enter is required after
entering a number. 

When the console has received its array size, it generates the etch-a-sketch. When 
looking at the board from the long breadboard side, the leftmost button moves the 
cursor up, second from the left is for moving the cursor down, second from the 
right is for moving the cursor left, and rightmost button is for moving the cursor
right.

Like before, pressing spacebar and then enter clears all drawing that has been done 
so far (with the exception of the current cursor position)

## Security
For security, I configured my bone so it could only be accessed on port 1010. I then 
made it so that fail2ban triggered a 15-second lockout when ssh is failed twice. 


# hw02 grading

| Points      | Description |
| ----------- | ----------- |
|  2/2 | Buttons and LEDs 
|  7/7 | Etch-a-Sketch works
|      | Measuring a gpio pin on an Oscilloscope 
|  2/2 | Questions answered
|  4/4 | Table complete
|  2/2 | gpiod
|      | Security
|  1/1 | ssh port
|  1/1 | iptables
|  1/1 | fail2ban
| 20/20   | **Total**

Nice videos.