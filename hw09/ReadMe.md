## What's here?
Two main files are here: readTest.py and demo.py.

The first one, readTest.py, can be run on its own in the terminal using python3.
It prints a reading of the MAX31820 temperature sensors to the terminal.

The second major file, demo.py, is supported by credentials.json and token.pickle.
It uses these files to access a google sheet, which it is able to edit. Each time 
it is ran (using ./demo.py) it reads the three temperature sensors and logs 
them in the google sheet in addition to the time. 

sheetsScreenshot.jpg is a picture file that shows the state of the google sheet
as of 8:17AM on 11/17/2021.

Link to Google Sheet: https://docs.google.com/spreadsheets/d/1AGbQwgR-XIxR-LwQ-O8FJuPdeU2glmY124VALBUCHgE/edit#gid=0

# hw09 grading

| Points      | Description |
| ----------- | ----------- |
|  0/5 | Timeline
|  3/3 | MAX31820
| 7/10 | Logging to Sheets | No plot
|  0/2 | Extras
| 10/20 | **Total**

*My comments are in italics. --may*

