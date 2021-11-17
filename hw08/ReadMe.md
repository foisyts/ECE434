## What's here?
PENDING - WILL FILL IN LATER

## Blinking an LED - questions 
What make command causes the LED code to run?
    -   The code is ran using "make TARGET=ledP9_31.pru0"
    
What make command stops the LED code from running?
    -   The code is stopped using "make TARGET=ledP9_31.pru0 stop"
    
The highest frequency that I attained was 12.48 MHz    
    
This waveform is slightly unstable and slightly jittery, with the 
instability and jitter increasing as the frequences increases. 

The file used for this part is ledP9_31.pru0.c 

## PWM Generator
The waveform produced using the pwm generator is much more stable 
when viewed at the specified 50MHZ It also has very near to 0 
jitter. 

My scope readings showed 0.0s for standard deviation, so the 
standard deviation is very near to zero. 

The file used for this part is pwm1.pru0.c, and it is executed 
using analogs to the commands described in part 1. 

## Table of Results 
Here is a table that compares the results for the PWM parts:

|File|Frequency|
| --- | --- |
|ledP9_31.pru0.c|12.48 MHz|
|file2|50 MHz|

 hw08 grading

| Points      | Description |
| ----------- | ----------- |
| 4/14 | PRU
|  0/2 | Controlling the PWM Frequency - optional
|  0/2 | Reading an Input at Regular Intervals - optional
|  0/2 | Analog Wave Generator - optional
|1/20 | **Total**

*My comments are in italics. --may*
