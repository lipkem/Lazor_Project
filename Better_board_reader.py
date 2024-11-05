import numpy as np
import re

'''
The Orig_Board_Processor class takes the original bff file 
provided by the puzzle and then does two things so far:
1- expands the original provided grid so that there is twice the number of spaces
    - x's in the original grid represent positions that cannot be occupied by blocks of any type
    - the laser can traverse any position other than opaque blocks (B blocks)
    - The odd columns and rows are positions that can be ocupied by blocks.
    - The even columns and rows are positions taht lasors can bounce off. 

2- finds the number of allowed blocks of each type
    - It looks for the part of the file that starts with A, B or C AFTER the GRID STOP language
    - the blocks in the grid are to be considered fixed in their position
    - the blocks identified by the "A,B or C" after the GRID STOP language are to be considered movable versions
    - The number of blocks identified after the grid do not include the fixed blocks in the grid itself. Example
    being showstopper 4- there isa fixed B block as well as 3 additional movable B blocks. 
    
3- finds the lasers in the bff file and reads them into a list of lists


'''

class Orig_Board_Processor:
    def __init__(self, filename):
        self.filename = filename
        self.list_by_line = []
        self.orig_grid_layout = []
        self.grid_for_solving_array = np.array([])
        self.number_of_A = 0
        self.number_of_B = 0
        self.number_of_C = 0
        self.lazors = []

    def read_file(self):
        """Read the BFF board file and store lines in a list."""
        with open(self.filename) as orig_board:
            content = orig_board.read()
            self.list_by_line = content.strip().split('\n')

    def extract_grid(self):
        """Extract the grid layout from the content."""
        start_index, stop_index = self.find_grid_indices()

        if start_index is not None and stop_index is not None:
            self.orig_grid_layout = [line.replace(' ', '') for line in self.list_by_line[start_index + 1:stop_index]]
        else:
            self.orig_grid_layout = []  # Handle the case where the lines aren't found

    def find_grid_indices(self):
        """Find the start and stop indices for the grid."""
        start_index = stop_index = None
        for i, line in enumerate(self.list_by_line):
            if "GRID START" in line:
                start_index = i
            elif "GRID STOP" in line:
                stop_index = i
        return start_index, stop_index

    def create_solving_grid(self):
        """Create the grid for solving based on the original layout."""
        if self.orig_grid_layout:
            max_width = (2 * len(self.orig_grid_layout[0]))+1
            height = (2 * len(self.orig_grid_layout))+1
            grid_for_solving = [['o' for _ in range(max_width)] for _ in range(height)]

            for row in range(len(self.orig_grid_layout)):
                for col in range(len(self.orig_grid_layout[row])):
                    grid_for_solving[row * 2 + 1][col * 2 + 1] = self.orig_grid_layout[row][col]

            self.grid_for_solving_array = np.array(grid_for_solving, dtype=object)

    def count_blocks(self):
        """Count the allowed number of blocks of each type (A, B, C)."""
        stop_index, _ = self.find_grid_indices()
        for line in self.list_by_line[stop_index:]:
            if line.startswith('A'):
                self.number_of_A = self.extract_number(line)
            elif line.startswith('B'):
                self.number_of_B = self.extract_number(line)
            elif line.startswith('C'):
                self.number_of_C = self.extract_number(line)

    def extract_number(self, line):
        """Extract the number following the block type from the line."""
        match = re.search(r'(\w)\s*(\d+)', line)
        return int(match.group(2)) if match else 0

    def extract_lazors(self):
        #This method will look in the bff file after the GRID STOP point and find the first 
        #instance where it sees L. It will load each line of numbers after L into a list of lists, representing our lazors
        stop_index, _ = self.find_grid_indices()
        lazor_index = 0
        for line in self.list_by_line[stop_index:]:
            if line.startswith('L'):
                lazor_index+1

        stop_index, _ = self.find_grid_indices()
        self.lazors = []  # Initialize the lazors list
        lazor_found = False

        for line in self.list_by_line[stop_index:]:
            if line.startswith('L'):
                # Split the line to get the numbers following 'L'
                numbers = list(map(int, line[1:].strip().split()))
                if len(numbers) == 4:  # Ensure exactly 4 numbers are present
                    self.lazors.append(numbers)  # Add the list of 4 numbers to lazors
                else:
                    print(f"Warning: Expected 4 numbers after 'L', found {len(numbers)} in line: {line}")
            elif self.lazors:
                # Stop collecting if we hit a line that doesn't start with 'L' after finding the first 'L'
                break

        if not self.lazors:
            print("No lazors found after GRID STOP.")
        # stop_index, _ = self.find_grid_indices()
        # self.lazors = []  # Initialize the lazors list
    
        # for line in self.list_by_line[stop_index:]:
        #     line = line.strip()  # Strip whitespace
        #     print(f"Processing line: '{line}'")  # Debug statement
    
        #     if line.startswith('L'):
        #         # Split the line to get the numbers following 'L'
        #         numbers = list(map(int, line[1:].strip().split()))
        #         if len(numbers) == 4:  # Ensure exactly 4 numbers are present
        #             self.lazors.append(numbers)  # Add the list of 4 numbers to lazors
        #             print(f"Found lazor: {numbers}")  # Debug statement
        #         else:
        #             print(f"Warning: Expected 4 numbers after 'L', found {len(numbers)} in line: {line}")
        #     elif self.lazors:  # Stop collecting if we hit a line that doesn't start with 'L'
        #         break
    
        # if not self.lazors:
        #     print("No lazors found after GRID STOP.")
    def extract_targets(self):
        #This will take the targets for the lazors outlined in the bff file and put them into a list of lists 
        stop_index, _ = self.find_grid_indices()
        target_index = 0
        for line in self.list_by_line[stop_index:]:
            if line.startswith('P'):
                target_index+1

        stop_index, _ = self.find_grid_indices()
        self.targets = []  # Initialize the targets list
        target_found = False

        for line in self.list_by_line[stop_index:]:
            if line.startswith('P'):
                # Split the line to get the numbers following 'L'
                numbers = list(map(int, line[1:].strip().split()))
                if len(numbers) == 2:  # Ensure exactly 2 numbers are present
                    self.targets.append(numbers)  # Add the list of 2 numbers to target
                else:
                    print(f"Warning: Expected 2 numbers after 'P', found {len(numbers)} in line: {line}")
            elif self.targets:
                # Stop collecting if we hit a line that doesn't start with 'L' after finding the first 'L'
                break

        if not self.targets:
            print("No targets found after GRID STOP.")
            
    def display_results(self):
        """Display the results of the processing."""
        print(f'Number of A blocks: {self.number_of_A}')
        print(f'Number of B blocks: {self.number_of_B}')
        print(f'Number of C blocks: {self.number_of_C}')
        print('Original grid layout:', self.orig_grid_layout)
        print('Grid for solving array:\n', self.grid_for_solving_array)
        print('Lazors:', self.lazors)
        print('Targets:', self.targets)

def main():
    processor = Orig_Board_Processor('dark_1.bff')
    processor.read_file()
    processor.extract_grid()
    processor.create_solving_grid()
    processor.count_blocks()
    processor.extract_lazors()
    processor.extract_targets()
    processor.display_results()
    

if __name__ == '__main__':
    main()
