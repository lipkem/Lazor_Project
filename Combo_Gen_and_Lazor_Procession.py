
from itertools import permutations
import numpy as np

# Initial matrix
matrix = np.array([['o', 'o', 'o', 'o', 'o', 'o', 'o'],
                   ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
                   ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
                   ['o', 'o', 't', 'o', 'o', 'o', 'o'],
                   ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
                   ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
                   ['o', 'o', 'o', 'o', 'o', 'o', 'o']])

# Parameters for specific counts of A, B, and C
num_a = 2  # Example number of A's
num_b = 1  # Example number of B's
num_c = 1  # Example number of C's

# Step 1: Identify odd-indexed 'o' positions
odd_positions = []
for row in range(matrix.shape[0]):
    for col in range(matrix.shape[1]):
        if row % 2 == 1 and col % 2 == 1 and matrix[row, col] == 'o':
            odd_positions.append((row, col))

# Check if the number of required positions matches with counts of A, B, and C
total_items = num_a + num_b + num_c
if len(odd_positions) < total_items:
    print("Not enough odd 'o' positions to place all A, B, and C items.")
else:
    # Step 2: Generate the list of items to place, including placeholders if necessary
    items = ['A'] * num_a + ['B'] * num_b + ['C'] * num_c
    placeholders_needed = len(odd_positions) - total_items
    items += [''] * placeholders_needed  # Add empty strings as placeholders

    # Step 3: Generate all unique permutations of these items in the odd positions
    unique_combinations = set(permutations(items))

    # Step 4: Store matrices for each unique combination in a list
    result_matrices = []
    for combo in unique_combinations:
        # Create a copy of the matrix to apply this combination
        new_matrix = matrix.copy()
        for pos, item in zip(odd_positions, combo):
            if item:  # Place only non-placeholder items
                new_matrix[pos] = item
        result_matrices.append(new_matrix)

# print(result_matrices)

formatted_matrices = np.array([matrix.tolist() for matrix in result_matrices])
print(formatted_matrices)
# print(len(formatted_matrices))

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
#                        ['o', 'o', 't', 'o', 'o', 'o', 'o'],
#                        ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#                        ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#                        ['o', 'o', 'o', 'o', 'o', 'o', 'o']])


Lazors = [[0, 1, 1, 1], [5, 0, -1, 1]]
Targets = [[2, 3]]
A = 1
B = 1
C = 1

print(Lazors)
for test_array in Combinations:
    lazor_array = np.array(  # Define an array that is the same as the combination board, this will be for lazor procession
        [['o']*test_array.shape[1]]*test_array.shape[0])
    for n in Targets:  # Itterate over the targets, placing a t for every target on our lazor array
        lazor_array[n[1]][n[0]] = 't'

    for L in Lazors:  # Cycle through the Lazors
        # Label Lasers as L on the array just created, not necessary but a good check, may end up erased if other laser crosses
        lazor_array[L[1]][L[0]] = 'L'
        print(L)
        while ([False] == [(L[0] <= 0) & (L[2] == -1)] and  # Checking x and vx to make sure we will not go over Left border
               # Checking x and vx to make sure we will not go over Left border
               [False] == [(L[0] >= (test_array.shape[1]-1)) & (L[2] == 1)] and
               # Checking y and vy to make sure we will not go over top border
               [False] == [(L[1] <= 0) & (L[3] == -1)] and
               # Checking y and vy to make sure we will not go over bottom border
               [False] == [(L[1] >= (test_array.shape[0]-1)) & (L[3] == 1)]):
            # If y is even (ie the laser is currently on top of a box, not on the side)
            if L[1] % 2 == 0:
                if L[2] == 1:  # If x vector is positive
                    if L[3] == 1:  # If y vector is positive
                        # If block immediately beneath is open or 'x'
                        if test_array[L[1]+1][L[0]] == 'o' or test_array[L[1]+1][L[0]] == 'x':
                            # Change next laser path box to '-', considered hit
                            lazor_array[L[1]+1][L[0]+1] = '-'
                            L[0] += 1  # Move laser to new location
                            L[1] += 1  # Move laser to new location
                        # If A block present, change the y direction
                        elif test_array[L[1]+1][L[0]] == 'A':
                            L[3] *= -1
                        # If C block present, procede like o/x but also create new Lazer
                        elif test_array[L[1]+1][L[0]] == 'C':
                            new_L = L  # Need to figure out what to do here
                            # Need to figure out what to do with this laser
                            new_L[3] = -L[3]
                            lazor_array[L[1]+1][L[0]+1] = '-'
                            L[0] += 1
                            L[1] += 1
                        # If B block present, send Lazer off the array, essentially ending the process
                        elif test_array[L[1]+1][L[0]] == 'B':
                            L[0:1] = [-L[0]], [-L[1]]
                    if L[3] == -1:  # If y vector is negative
                        # If block immediately above is open or 'x'
                        if test_array[L[1]-1][L[0]] == 'o' or test_array[L[1]+1][L[0]] == 'x':
                            # Change next laser path box to '-', considered hit
                            lazor_array[L[1]-1][L[0]+1] = '-'
                            L[0] += 1  # Move laser to new location
                            L[1] -= 1  # Move laser to new location
                        # If A block present, change the y direction
                        elif test_array[L[1]-1][L[0]] == 'A':
                            L[3] *= -1
                        # If C block present, procede like o/x but also create new Lazer
                        elif test_array[L[1]-1][L[0]] == 'C':
                            new_L = L  # Need to figure out what to do here
                            # Need to figure out what to do with this laser
                            new_L[3] = -L[3]
                            lazor_array[L[1]-1][L[0]+1] = '-'
                            L[0] += 1
                            L[1] -= 1
                        # If B block present, send Lazer off the array, essentially ending the process
                        elif test_array[L[1]-1][L[0]] == 'B':
                            L[0:1] = [-L[0]], [-L[1]]
                if L[2] == - 1:  # If x vector is negative
                    if L[3] == 1:  # If y vector is positive
                        # If block immediately beneath is open or 'x'
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
                            new_L = L  # Need to figure out what to do here
                            # Need to figure out what to do with this laser
                            new_L[3] = -L[3]
                            lazor_array[L[1]+1][L[0]-1] = '-'
                            L[0] += 1
                            L[1] += 1
                        # If B block present, send Lazer off the array, essentially ending the process
                        elif test_array[L[1]+1][L[0]] == 'B':
                            L[0:1] = [-L[0]], [-L[1]]
                    if L[3] == -1:  # If y vector is negative
                        # If block immediately below is open or 'x'
                        if test_array[L[1]-1][L[0]] == 'o' or test_array[L[1]+1][L[0]] == 'x':
                            # Change next laser path box to '-', considered hit
                            lazor_array[L[1]-1][L[0]-1] = '-'
                            L[0] -= 1  # Move laser to new location
                            L[1] -= 1  # Move laser to new location
                        # If A block present, change the y direction
                        elif test_array[L[1]-1][L[0]] == 'A':
                            L[3] *= -1
                        # If C block present, procede like o/x but also create new Lazer
                        elif test_array[L[1]-1][L[0]] == 'C':
                            new_L = L  # Need to figure out what to do here
                            # Need to figure out what to do with this laser
                            new_L[3] = -L[3]
                            lazor_array[L[1]-1][L[0]-1] = '-'
                            L[0] -= 1
                            L[1] -= 1
                        # If B block present, send Lazer off the array, essentially ending the process
                        elif test_array[L[1]-1][L[0]] == 'B':
                            L[0:1] = [-L[0]], [-L[1]]
            # If x cordinate is even (ie laser is on side of block)
            elif L[0] % 2 == 0:
                if L[2] == 1:  # If x vector is positive
                    if L[3] == 1:  # If y vector is positive
                        # If block immediately right is open or 'x'
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
                            new_L = L  # Need to figure out what to do here
                            # Need to figure out what to do with this laser
                            new_L[2] = -L[2]
                            lazor_array[L[1]+1][L[0]+1] = '-'
                            L[0] += 1
                            L[1] += 1
                        # If B block present, send Lazer off the array, essentially ending the process
                        elif test_array[L[1]][L[0]+1] == 'B':
                            # making them negative to stop the while loop
                            L[0:1] = [-L[0]], [-L[1]]

                    if L[3] == -1:  # If y vector is positive
                        # If block immediately right is open or 'x'
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
                            new_L = L  # Need to figure out what to do here
                            # Need to figure out what to do with this laser
                            new_L[2] = -L[2]
                            lazor_array[L[1]-1][L[0]+1] = '-'
                            L[0] += 1
                            L[1] -= 1
                        # If B block present, send Lazer off the array, essentially ending the process
                        elif test_array[L[1]][L[0]+1] == 'B':
                            # making them negative to stop the while loop
                            L[0:1] = [-L[0]], [-L[1]]
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
                            new_L = L  # Need to figure out what to do here
                            # Need to figure out what to do with this laser
                            new_L[2] = -L[2]
                            lazor_array[L[1]+1][L[0]-1] = '-'
                            L[0] -= 1
                            L[1] += 1
                        # If B block present, send Lazer off the array, essentially ending the process
                        elif test_array[L[1]][L[0]-1] == 'B':
                            # making them negative to stop the while loop
                            L[0:1] = [-L[0]], [-L[1]]

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
                            new_L = L  # Need to figure out what to do here
                            # Need to figure out what to do with this laser
                            new_L[2] = -L[2]
                            lazor_array[L[1]-1][L[0]-1] = '-'
                            L[0] -= 1
                            L[1] -= 1
                        # If B block present, send Lazer off the array, essentially ending the process
                        elif test_array[L[1]][L[0]-1] == 'B':
                            # making them negative to stop the while loop
                            L[0:1] = [-L[0]], [-L[1]]

    if "t" in lazor_array:
        print("not a solution")
    else:
        print("Solution Found")
        print(lazor_array)