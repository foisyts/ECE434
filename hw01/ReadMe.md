##What the "hw01.py" file does:
	Running this file allows the user to use a simple Etch-a-sketch
	program in the terminal where it is ran. It takes keyboard input
	from the user and uses that to draw an image based on current 
	cursor position. The keyboard can also be used to clear the 
	screen. To implement this, I constructed a 2D array and kept 
	track of cursor position after a key was pressed. Key inputs 
	were handled with the Python "input()" function. Initialization,
	clearing, and drawing the array are handled with nested loops.

##How to use the "hw01.py" file:
	First, the file must be booted in a console (ie. enter the 
	command python3 hw01.py in the correct directory). Then, the 
	user is prompted for a matrix size, specified by entering a 
	number key (1,6, 10, etc) and then pressing enter.
	
	After that, the Etch-a-sketch will start. The cursor starts 
	in the upper right-hand corner and can be moved by pressing 
	the w,a,s, and d keys. Pressing enter is required after each
	key entry. The spacebar can be pressed as well - doing so
	clears the grid, except for where the cursor is currently.
	Again, the enter key needs to be pressed after pressing 
	spacebar.

	The program does not do anything to handle any other keys
	being pressed: it only deals with the production of "w", 
	"a", "s", "d", and " ".

	To exit the Etch-a-sketch, the user must press ctrl+c. 
