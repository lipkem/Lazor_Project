
# from itertools import combinations_with_replacement, permutations
# from itertools import permutations
# import numpy as np

# # Initial matrix
# matrix = np.array([
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o']
# ])

# # matrix = np.array([
# #     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
# #     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
# #     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
# #     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
# #     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
# #     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
# #     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
# #     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
# #     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
# # ])

# # Parameters for specific counts of A, B, and C
# num_a = 2  # Example number of A's
# num_b = 1  # Example number of B's
# num_c = 1  # Example number of C's

# # Step 1: Identify odd-indexed 'o' positions
# odd_positions = []
# for row in range(matrix.shape[0]):
#     for col in range(matrix.shape[1]):
#         if row % 2 == 1 and col % 2 == 1 and matrix[row, col] == 'o':
#             odd_positions.append((row, col))

# # Check if the number of required positions matches with counts of A, B, and C
# total_items = num_a + num_b + num_c
# if len(odd_positions) < total_items:
#     print("Not enough odd 'o' positions to place all A, B, and C items.")
# else:
#     # Step 2: Generate the list of items to place, including placeholders if necessary
#     items = ['A'] * num_a + ['B'] * num_b + ['C'] * num_c
#     placeholders_needed = len(odd_positions) - total_items
#     items += [''] * placeholders_needed  # Add empty strings as placeholders

#     # Step 3: Generate all unique permutations of these items in the odd positions
#     unique_combinations = set(permutations(items))

#     # Step 4: Store matrices for each unique combination in a list
#     result_matrices = []
#     for combo in unique_combinations:
#         # Create a copy of the matrix to apply this combination
#         new_matrix = matrix.copy()
#         for pos, item in zip(odd_positions, combo):
#             if item:  # Place only non-placeholder items
#                 new_matrix[pos] = item
#         result_matrices.append(new_matrix)

# # print(result_matrices)

# formatted_matrices = np.array([matrix.tolist() for matrix in result_matrices])
# print(formatted_matrices)
# print(len(formatted_matrices))

# #################################################

# from itertools import combinations_with_replacement, permutations
# from itertools import permutations
# import numpy as np


# # Initial matrix
# # matrix = np.array([
# #     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
# #     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
# #     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
# #     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
# #     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
# #     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
# #     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
# #     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
# #     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
# # ])

# matrix = np.array([
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o']
# ])

# # Parameters for specific counts of A, B, and C
# num_a = 2  # Example number of A's
# num_b = 1  # Example number of B's
# num_c = 1  # Example number of C's

# # Step 1: Identify odd-indexed 'o' positions
# odd_positions = []
# for row in range(matrix.shape[0]):
#     for col in range(matrix.shape[1]):
#         if row % 2 == 1 and col % 2 == 1 and matrix[row, col] == 'o':
#             odd_positions.append((row, col))

# # Check if the number of required positions matches with counts of A, B, and C
# total_items = num_a + num_b + num_c
# if len(odd_positions) < total_items:
#     print("Not enough odd 'o' positions to place all A, B, and C items.")
# else:
#     # Step 2: Generate the list of items to place, including placeholders if necessary
#     items = ['A'] * num_a + ['B'] * num_b + ['C'] * num_c
#     placeholders_needed = len(odd_positions) - total_items
#     items += [''] * placeholders_needed  # Add placeholders

#     # Step 3: Generate all unique combinations of placements
#     # Find unique combinations by treating identical items (e.g., two A's) the same
#     unique_combinations = set(permutations(items))

#     # Step 4: Store matrices for each unique combination in a list
#     result_matrices = []
#     for combo in unique_combinations:
#         # Create a copy of the matrix to apply this combination
#         new_matrix = matrix.copy()
#         for pos, item in zip(odd_positions, combo):
#             if item:  # Place only non-placeholder items
#                 new_matrix[pos] = item
#         result_matrices.append(new_matrix)

#     # Print result matrices (limit output for readability)
#     print(f"Generated {len(result_matrices)} unique configurations.")
#     # Display only first 10 samples
#     for i, res_matrix in enumerate(result_matrices[:10], 1):
#         print(f"Matrix {i}:\n{res_matrix}\n")

# formatted_matrices = np.array([matrix.tolist() for matrix in result_matrices])
# print(formatted_matrices)
# print(len(formatted_matrices))

# ####################################################


# from itertools import permutations, combinations
# import numpy as np

# # Initial matrix setup
# # matrix = np.array([
# #     ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
# #     ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
# #     ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
# #     ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
# #     ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
# #     ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
# #     ['o', 'o', 'o', 'o', 'o', 'o', 'o']
# # ])

# matrix = np.array([
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
# ])

# # Define number of items to place
# num_a = 2
# num_b = 1
# num_c = 1
# total_items = num_a + num_b + num_c

# # Step 1: Identify valid positions (e.g., odd-indexed positions)
# odd_positions = [(row, col) for row in range(matrix.shape[0]) for col in range(matrix.shape[1])
#                  if row % 2 == 1 and col % 2 == 1 and matrix[row, col] == 'o']

# # Check if there are enough valid positions
# if len(odd_positions) < total_items:
#     print("Not enough odd 'o' positions to place all A, B, and C items.")
# else:
#     # Step 2: Generate the items list and corresponding position combinations
#     items = ['A'] * num_a + ['B'] * num_b + ['C'] * num_c
#     position_combinations = combinations(odd_positions, total_items)

#     # Step 3: Generate and store matrices for each valid placement permutation
#     result_matrices = []
#     for positions in position_combinations:
#         # Generate all unique item arrangements for the chosen positions
#         for item_arrangement in set(permutations(items)):
#             # Copy the original matrix
#             new_matrix = matrix.copy()
#             # Place items in the selected positions
#             for pos, item in zip(positions, item_arrangement):
#                 new_matrix[pos] = item
#             result_matrices.append(new_matrix)

# # Optional: Convert results to list format if needed
# formatted_matrices = np.array([matrix.tolist() for matrix in result_matrices])
# print(formatted_matrices)
# print("Total unique configurations:", len(formatted_matrices))

# ABOVE WITH TIMER ####################################3
import time
from itertools import permutations, combinations
import numpy as np

# Start the timer
start_time = time.time()

# Initial matrix setup
# matrix = np.array([
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o'],
#     ['o', 'o', 'o', 'o', 'o', 'o', 'o']
# ])


matrix = np.array([
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
])

# Define number of items to place
num_a = 2
num_b = 1
num_c = 1
total_items = num_a + num_b + num_c

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
