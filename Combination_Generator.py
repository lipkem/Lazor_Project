from itertools import permutations
import numpy as np

# Initial matrix
matrix = np.array([
    ['o', 'x', 'o', 'o', 'o'],
    ['o', 'o', 'x', 'o', 'o'],
    ['x', 'o', 'o', 'o', 'o'],
    ['x', 'o', 'o', 'o', 'o'],
    ['x', 'o', 'o', 'o', 'o']
])

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

