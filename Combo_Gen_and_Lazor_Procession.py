#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 17:14:45 2024

@author: mitchelllipke
"""

import time
from itertools import permutations, combinations
import numpy as np
import copy

# Start the timer
start_time = time.time()

# Define number of items to place
num_a = 2
num_b = 0
num_c = 0
total_items = num_a + num_b + num_c

Lazors = [[2, 1, 1, -1]]
Targets = [[3, 2]]


# Initial matrix setup
matrix = np.array([
    ['o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o'],
])


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

# End the timer
end_time = time.time()

# Calculate and print the elapsed time
execution_time = end_time - start_time
print(f"Execution Time: {execution_time:.2f} seconds")
print("Total unique configurations:", len(formatted_matrices))


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

    for L in temp_Lazors:  # Cycle through the Lazors
        # Label Lasers as L on the array just created, not necessary but a good check, may end up erased if other laser crosses
        # for test_array in Combinations:
        for n in Targets:  # Itterate over the targets, placing a t for every target on our lazor array
            lazor_array[n[1]][n[0]] = 't'
        lazor_array[L[1]][L[0]] = 'L'
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
    print(count)

    if "t" in lazor_array:
        print("not a solution")
    else:
        print("Solution Found")
        print(lazor_array)
        print(test_array)

