#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import numpy as np
from itertools import permutations, combinations
import time
import re


####################################################################
A = 'XXXXXXXXXXXX.bff'  #### PLEASE PUT FILE NAME IN PLACE OF Xs####
####################################################################

# Start the timer
start_time = time.time()


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
            self.orig_grid_layout = [line.replace(
                ' ', '') for line in self.list_by_line[start_index + 1:stop_index]]
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
            grid_for_solving = [
                ['o' for _ in range(max_width)] for _ in range(height)]

            for row in range(len(self.orig_grid_layout)):
                for col in range(len(self.orig_grid_layout[row])):
                    grid_for_solving[row * 2 + 1][col * 2 +
                                                  1] = self.orig_grid_layout[row][col]

            self.grid_for_solving_array = np.array(
                grid_for_solving, dtype=object)

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
        # This method will look in the bff file after the GRID STOP point and find the first
        # instance where it sees L. It will load each line of numbers after L into a list of lists, representing our lazors
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
                    # Add the list of 4 numbers to lazors
                    self.lazors.append(numbers)
                else:
                    print(f"Warning: Expected 4 numbers after 'L', found {
                          len(numbers)} in line: {line}")

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
        # This will take the targets for the lazors outlined in the bff file and put them into a list of lists
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
                    # Add the list of 2 numbers to target
                    self.targets.append(numbers)
                else:
                    print(f"Warning: Expected 2 numbers after 'P', found {
                          len(numbers)} in line: {line}")

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
    processor = Orig_Board_Processor(A)
    processor.read_file()
    processor.extract_grid()
    processor.create_solving_grid()
    processor.count_blocks()
    processor.extract_lazors()
    processor.extract_targets()
    processor.display_results()
    return processor


if __name__ == '__main__':
    processor = main()

#######################  MARKS CODE  ###################################

# Define number of items to place
    num_a = processor.number_of_A
    num_b = processor.number_of_B
    num_c = processor.number_of_C

    Lazors = processor.lazors
    Targets = processor.targets


# Initial matrix setup
matrix = np.array(processor.grid_for_solving_array)

total_items = num_a + num_b + num_c


# matrix = np.array([
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
# ])


# Step 1: Identify valid positions (e.g., odd-indexed positions)
odd_positions = [(row, col) for row in range(matrix.shape[0]) for col in range(matrix.shape[1])
                 if row % 2 == 1 and col % 2 == 1 and matrix[row, col] == 'o']

# Check if there are enough valid positions
if len(odd_positions) < total_items:
    print("Not enough odd 'o' positions to place all A, B, and C items.")
else:
    # Step 2: Generate the items list and corresponding position combinations
    items = ['A'] * num_a + ['B'] * num_b + ['C'] * num_c
    position_combinations = combinations(odd_positions, total_items)

    # Step 3: Generate and store matrices for each valid placement permutation
    result_matrices = []
    for positions in position_combinations:
        # Generate all unique item arrangements for the chosen positions
        for item_arrangement in set(permutations(items)):
            # Copy the original matrix
            new_matrix = matrix.copy()
            # Place items in the selected positions
            for pos, item in zip(positions, item_arrangement):
                new_matrix[pos] = item
            result_matrices.append(new_matrix)


# Optional: Convert results to list format if needed
formatted_matrices = np.array([matrix.tolist() for matrix in result_matrices])

print("Finished generating combinations")

Combinations = formatted_matrices

# Combinations = [np.array([['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#                           ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#                           ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#                           ['o', 'o', 't', 'o', 'o', 'o', 'o'],
#                           ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#                           ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#                           ['o', 'o', 'o', 'o', 'o', 'o', 'o']]),
#                 np.array([['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#                           ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#                           ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#                           ['o', 'o', 't', 'o', 'o', 'o', 'o'],
#                           ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#                           ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#                           ['o', 'o', 'o', 'o', 'o', 'o', 'o']])]

# test_array = np.array([['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#                        ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#                        ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#                        ['o', 'A', 'o', 'o', 'o', 'o', 'o'],
#                        ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#                        ['o', 'o', 'o', 'C', 'o', 'o', 'o'],
#                        ['o', 'o', 'o', 'o', 'o', 'o', 'o']])


# Lazors = [[3, 2, -1, 1]]
# Targets = [[6, 6]]
# # L = [1, 0, 1, 1]
# A = 1
# B = 1
# C = 1

count = 0
for test_array in Combinations:
    lazor_array = np.array(  # Define an array that is the same as the combination board, this will be for lazor procession
        [['o']*test_array.shape[1]]*test_array.shape[0])
    temp_Lazors = copy.deepcopy(Lazors)
    for n in Targets:  # Itterate over the targets, placing a t for every target on our lazor array
        lazor_array[n[1]][n[0]] = 't'
    for L in temp_Lazors:  # Cycle through the Lazors
        # Label Lasers as L on the array just created, not necessary but a good check, may end up erased if other laser crosses
        # for test_array in Combinations:
        lazor_array[L[1]][L[0]] = 'L'
        step_counter = 0
        while (([False] == [(L[0] <= 0) & (L[2] == -1)]) and  # Checking x and vx to make sure we will not go over Left border
               # Checking x and vx to make sure we will not go over Left border
               ([False] == [(L[0] >= (test_array.shape[1]-1)) & (L[2] == 1)]) and
               # Checking x and vx to make sure we will not go over top border
               ([False] == [(L[1] <= 0) & (L[3] == -1)]) and
               # Checking y and vy to make sure we will not go over bottom border
               ([False] == [(L[1] >= (test_array.shape[0]-1)) & (L[3] == 1)]) and
               # Aribitaily allow 50 Lazor steps
               (step_counter <= 50) and
               (len(temp_Lazors) <= 50)):  # Limit new Lazor creations (ie refractions)
            # If y is even (ie the laser is currently on top of a box, not on the side)
            step_counter += 1
            print("Checking " + str(count) + " out of " +
                  str(len(formatted_matrices)))
            if L[1] % 2 == 0:
                if L[2] == 1:  # If x vector is positive
                    if L[3] == 1:  # If y vector is positive
                        # If block immediately beneath is open or 'x'
                        if (test_array[L[1]+1][L[0]] == 'o' or test_array[L[1]+1][L[0]] == 'x'):
                            # Change next laser path box to '-', considered hit
                            lazor_array[L[1]+1][L[0]+1] = '-'
                            L[0] += 1  # Move laser to new location
                            L[1] += 1  # Move laser to new location
                        # If A block present, change the y direction
                        elif test_array[L[1]+1][L[0]] == 'A':
                            L[3] *= -1
                        # If C block present, procede like o/x but also create new Lazer
                        elif test_array[L[1]+1][L[0]] == 'C':
                            new_L = L.copy()  # Need to figure out what to do here
                            # Need to figure out what to do with this laser
                            new_L[3] *= -1
                            temp_Lazors.append(new_L)
                            lazor_array[L[1]+1][L[0]+1] = '-'
                            L[0] += 1
                            L[1] += 1

                        # If B block present, send Lazer off the array, essentially ending the process
                        elif test_array[L[1]+1][L[0]] == 'B':
                            lazor_active = False  # Stop processing this Lazor
                            break  # Break out of the inner loop for this Lazor
                    if L[3] == -1:  # If y vector is negative
                        # If block immediately above is open or 'x'
                        if (test_array[L[1]-1][L[0]] == 'o' or test_array[L[1]-1][L[0]] == 'x'):
                            # Change next laser path box to '-', considered hit
                            lazor_array[L[1]-1][L[0]+1] = '-'
                            L[0] += 1  # Move laser to new location
                            L[1] -= 1  # Move laser to new location
                        # If A block present, change the y direction
                        elif test_array[L[1]-1][L[0]] == 'A':
                            L[3] *= -1
                        # If C block present, procede like o/x but also create new Lazer
                        elif test_array[L[1]-1][L[0]] == 'C':
                            new_L = L.copy()  # Need to figure out what to do here
                            # Need to figure out what to do with this laser
                            new_L[3] *= -1
                            temp_Lazors.append(new_L)
                            lazor_array[L[1]-1][L[0]+1] = '-'
                            L[0] += 1
                            L[1] -= 1

                        # If B block present, send Lazer off the array, essentially ending the process
                        elif test_array[L[1]-1][L[0]] == 'B':
                            lazor_active = False  # Stop processing this Lazor
                            break  # Break out of the inner loop for this Lazor
                if L[2] == - 1:  # If x vector is negative
                    if L[3] == 1:  # If y vector is positive
                        # If block immediately beneath is open or 'x'
                        # or L[1] == (test_array.shape[0]-2) or L[0] == 1:
                        if test_array[L[1]+1][L[0]] == 'o' or test_array[L[1]+1][L[0]] == 'x':
                            # Change next laser path box to '-', considered hit
                            lazor_array[L[1]+1][L[0]-1] = '-'
                            L[0] -= 1  # Move laser to new location
                            L[1] += 1  # Move laser to new location
                        # If A block present, change the y direction
                        elif test_array[L[1]+1][L[0]] == 'A':
                            L[3] *= -1
                        # If C block present, procede like o/x but also create new Lazer
                        elif test_array[L[1]+1][L[0]] == 'C':
                            new_L = L.copy()  # Need to figure out what to do here
                            # Need to figure out what to do with this laser
                            new_L[3] *= -1
                            temp_Lazors.append(new_L)
                            lazor_array[L[1]+1][L[0]-1] = '-'
                            L[0] += 1
                            L[1] += 1

                        # If B block present, send Lazer off the array, essentially ending the process
                        elif test_array[L[1]+1][L[0]] == 'B':
                            lazor_active = False  # Stop processing this Lazor
                            break  # Break out of the inner loop for this Lazor
                    if L[3] == -1:  # If y vector is negative
                        # If block immediately below is open or 'x'
                        # or L[1] == 1 or L[0] == 1:
                        if test_array[L[1]-1][L[0]] == 'o' or test_array[L[1]-1][L[0]] == 'x':
                            # Change next laser path box to '-', considered hit
                            lazor_array[L[1]-1][L[0]-1] = '-'
                            L[0] -= 1  # Move laser to new location
                            L[1] -= 1  # Move laser to new location
                        # If A block present, change the y direction
                        elif test_array[L[1]-1][L[0]] == 'A':
                            L[3] *= -1
                        # If C block present, procede like o/x but also create new Lazer
                        elif test_array[L[1]-1][L[0]] == 'C':
                            new_L = L.copy()  # Need to figure out what to do here
                            # Need to figure out what to do with this laser
                            new_L[3] *= -1
                            temp_Lazors.append(new_L)
                            lazor_array[L[1]-1][L[0]-1] = '-'
                            L[0] -= 1
                            L[1] -= 1

                        # If B block present, send Lazer off the array, essentially ending the process
                        elif test_array[L[1]-1][L[0]] == 'B':
                            lazor_active = False  # Stop processing this Lazor
                            break  # Break out of the inner loop for this Lazor
            # If x cordinate is even (ie laser is on side of block)
            elif L[0] % 2 == 0:
                if L[2] == 1:  # If x vector is positive
                    if L[3] == 1:  # If y vector is positive
                        # If block immediately right is open or 'x'
                        # or L[1] == (test_array.shape[0]-2) or L[0] == (test_array.shape[1]-2):
                        if test_array[L[1]][L[0]+1] == 'o' or test_array[L[1]][L[0]+1] == 'x':
                            # Change next laser path box to '-', considered hit
                            lazor_array[L[1]+1][L[0]+1] = '-'
                            L[0] += 1  # Move laser to new location
                            L[1] += 1  # Move laser to new location
                        # If A block present, change the x direction
                        elif test_array[L[1]][L[0]+1] == 'A':
                            L[2] *= -1
                        # If C block present, procede like o/x but also create new Lazer
                        elif test_array[L[1]][L[0]+1] == 'C':
                            new_L = L.copy()  # Need to figure out what to do here
                            # Need to figure out what to do with this laser
                            new_L[2] *= -1
                            temp_Lazors.append(new_L)
                            lazor_array[L[1]+1][L[0]+1] = '-'
                            L[0] += 1
                            L[1] += 1

                        # If B block present, send Lazer off the array, essentially ending the process
                        elif test_array[L[1]][L[0]+1] == 'B':
                            lazor_active = False  # Stop processing this Lazor
                            break  # Break out of the inner loop for this Lazor

                    if L[3] == -1:  # If y vector is negative
                        # If block immediately right is open or 'x'
                        # or L[1] == 1 or L[0] == 1::
                        if test_array[L[1]][L[0]+1] == 'o' or test_array[L[1]][L[0]+1] == 'x':
                            # Change next laser path box to '-', considered hit
                            lazor_array[L[1]-1][L[0]+1] = '-'
                            L[0] += 1  # Move laser to new location
                            L[1] -= 1  # Move laser to new location
                        # If A block present, change the x direction
                        elif test_array[L[1]][L[0]+1] == 'A':
                            L[2] *= -1
                        # If C block present, procede like o/x but also create new Lazer
                        elif test_array[L[1]][L[0]+1] == 'C':
                            new_L = L.copy()  # Need to figure out what to do here
                            # Need to figure out what to do with this laser
                            new_L[2] *= -1
                            temp_Lazors.append(new_L)
                            lazor_array[L[1]-1][L[0]+1] = '-'
                            L[0] += 1
                            L[1] -= 1

                        # If B block present, send Lazer off the array, essentially ending the process
                        elif test_array[L[1]][L[0]+1] == 'B':
                            lazor_active = False  # Stop processing this Lazor
                            break  # Break out of the inner loop for this Lazor
                if L[2] == -1:  # If x vector is negative
                    if L[3] == 1:  # If y vector is positive
                        # If block immediately left is open or 'x'
                        if test_array[L[1]][L[0]-1] == 'o' or test_array[L[1]][L[0]-1] == 'x':
                            # Change next laser path box to '-', considered hit
                            lazor_array[L[1]+1][L[0]-1] = '-'
                            L[0] -= 1  # Move laser to new location
                            L[1] += 1  # Move laser to new location
                        # If A block present, change the x direction
                        elif test_array[L[1]][L[0]-1] == 'A':
                            L[2] *= -1
                        # If C block present, procede like o/x but also create new Lazer
                        elif test_array[L[1]][L[0]-1] == 'C':
                            new_L = L.copy()  # Need to figure out what to do here
                            # Need to figure out what to do with this laser
                            new_L[2] *= -1
                            temp_Lazors.append(new_L)
                            lazor_array[L[1]+1][L[0]-1] = '-'
                            L[0] -= 1
                            L[1] += 1

                        # If B block present, send Lazer off the array, essentially ending the process
                        elif test_array[L[1]][L[0]-1] == 'B':
                            lazor_active = False  # Stop processing this Lazor
                            break  # Break out of the inner loop for this Lazor

                    if L[3] == -1:  # If y vector is negative
                        # If block immediately right is open or 'x'
                        if test_array[L[1]][L[0]-1] == 'o' or test_array[L[1]][L[0]-1] == 'x':
                            # Change next laser path box to '-', considered hit
                            lazor_array[L[1]-1][L[0]-1] = '-'
                            L[0] -= 1  # Move laser to new location
                            L[1] -= 1  # Move laser to new location
                        # If A block present, change the x direction
                        elif test_array[L[1]][L[0]-1] == 'A':
                            L[2] *= -1
                        # If C block present, procede like o/x but also create new Lazer
                        elif test_array[L[1]][L[0]-1] == 'C':
                            new_L = L.copy()  # Need to figure out what to do here
                            # Need to figure out what to do with this laser
                            new_L[2] *= -1
                            temp_Lazors.append(new_L)
                            lazor_array[L[1]-1][L[0]-1] = '-'
                            L[0] -= 1
                            L[1] -= 1

                        # If B block present, send Lazer off the array, essentially ending the process
                        elif test_array[L[1]][L[0]-1] == 'B':
                            lazor_active = False  # Stop processing this Lazor
                            break  # Break out of the inner loop for this Lazor

    count += 1
    # print(count)

    if "t" not in lazor_array:
        print("Solution Found")
    #    print(lazor_array)
        print(count)
        print(test_array)
        SOLUTION = test_array

    # if (test_array[1][1] == 'B') & (test_array[3][1] == 'A') & (test_array[5][1] == 'B') & (test_array[7][1] == 'A') & (test_array[9][1] == 'B'):
    #     SOLUTION = "Success"
    # else:
    #     print("Not a Solution")
    #     print(lazor_array)
    #     print(test_array)


# End the timer
end_time = time.time()

# Calculate and print the elapsed time
execution_time = end_time - start_time
print(f"Execution Time: {execution_time:.2f} seconds")
print("Total unique configurations:", len(formatted_matrices))

print(SOLUTION)
