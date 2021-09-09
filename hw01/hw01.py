import os

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

# Specifies the start position for the cursor the leftmost 2 columns and the  
# top row are reserved to give the grid numbers to make it more visually 
# appealing
current_width = 2
current_height = 1

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

# Loop to read keyboard input and update the display of the grid on the console
while(1):
	dir = input("Press a WASD key to move the Etch-A-Sketch! (or Spacebar to clear)")
	if(dir == "w"):
		if(current_height > 1):
			current_height-= 1
	if(dir == "a"):
		if(current_width > 2):
			current_width -= 1
	if(dir == "s"):
		if(current_height < (size)):
			current_height+= 1
	if(dir == "d"):
		if(current_width < (size+1)):
			current_width += 1
	if(dir == " "):
		clear_etcher()
	array[current_height][current_width] = "X"
	update_output()
