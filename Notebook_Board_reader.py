
#This is a script to read the bff board file and convert it into a format that the solver can handle
#first we open the board
#orig_board = open('dark_1.bff')

#importing numpy package for the array handling and math features we anticipate using
import numpy as np

#opening the bff board file, and reading its contents into a string called "content"
with open('dark_1.bff') as orig_board:
    content = orig_board.read()  

#going through each line of this content string and stripping out the blank space. 
#Then, splitting it by line breaks
list_by_line = content.strip().split('\n')
grid_line_start = None
grid_line_stop = None

# a for loop that goes through each line and finds the position of the start and stop of the board grid
for i, line in enumerate(list_by_line):
    if "GRID START" in line:
        start_index = i
    elif "GRID STOP" in line:
        stop_index = i

# here i create a list of lists that only contains the grid layout from the original file
# This will be used to generate the expanded grid we will use to solve the puzzle
# the max_width and height variables are twice the size of those respective dimensions in the 
# original board. We will expand the grid to make our math easier when solving.

if start_index is not None and stop_index is not None:
        orig_grid_layout = [line.replace(' ', '') for line in list_by_line[start_index + 1:stop_index]]  # Remove spaces
else:
    orig_grid_layout = []  # Handle the case where the lines aren't found

if orig_grid_layout:  # Check if the list is not empty
    max_width = 2 * len(orig_grid_layout[0]) 
    height = 2 * len(orig_grid_layout)
else:
    max_width = 0
    height = 0

# Create the array that we will actually use to solve the puzzle. 
# We initially fill it entirely with 'o' in every position and will populate 
# with the original board file characters after. The grid for solving is twice the original gird's size in 
# both dimensions, and the original grid characters are placed at the odd numbered columns in the grid for solving
# This means in numpy array, the 0th row and 0 column will have first character from the original grid's first row
# The 0th row and the 2 column will have the second character from the original grid's first row and so on.

grid_for_solving = [['o' for _ in range(max_width)] for _ in range(height)]

for row in range(len(orig_grid_layout)):
    for col in range(len(orig_grid_layout[row])):
        grid_for_solving[row * 2][col * 2] = orig_grid_layout[row][col]

#converting it to a numpy array 
grid_for_solving_array = np.array(grid_for_solving, dtype=object)

print(orig_grid_layout)
print(grid_for_solving_array)






