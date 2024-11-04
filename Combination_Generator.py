# from itertools import permutations, product
# from itertools import permutations
# import numpy as np

# # Define the initial 2D matrix
# matrix = np.array([
#     ['o', 'x', 'o', 'o', 'o'],
#     ['o', 'o', 'x', 'o', 'o'],
#     ['x', 'o', 'o', 'o', 'o'],
#     ['x', 'o', 'o', 'o', 'o'],
#     ['x', 'o', 'o', 'o', 'o']
# ])

# # Define the exact occurrences for "A", "B", and "C"
# exact_counts = {"A": 1, "B": 1, "C": 1}

# # Find the positions of all "o" elements in the matrix
# o_positions = [(i, j) for i in range(len(matrix))
#                for j in range(len(matrix[0])) if matrix[i][j] == 'o']

# # Calculate the total number of "o" slots and create the exact combination list
# total_o_slots = len(o_positions)
# required_chars = (
#     ["A"] * exact_counts["A"] +
#     ["B"] * exact_counts["B"] +
#     ["C"] * exact_counts["C"] +
#     # Fill remaining slots with "o"
#     ['o'] * (total_o_slots - sum(exact_counts.values()))
# )

# # Generate all unique permutations of the required characters
# unique_combinations = set(permutations(required_chars))

# # Apply each valid combination to create new versions of the matrix
# results = []
# for combo in unique_combinations:
#     # Create a deep copy of the original matrix
#     temp_matrix = [row[:] for row in matrix]
#     # Replace "o" positions with elements from the combination
#     for (i, j), value in zip(o_positions, combo):
#         temp_matrix[i][j] = value
#     results.append(temp_matrix)

# # Print results
# for result in results:
#     for row in result:
#         print(row)
#     print()  # Separate different configurations

#########
# from itertools import permutations
# from itertools import permutations, product
# import numpy as np

# # Initial matrix
# matrix = np.array([
#     ['o', 'x', 'o', 'o', 'o'],
#     ['o', 'o', 'x', 'o', 'o'],
#     ['x', 'o', 'o', 'o', 'o'],
#     ['x', 'o', 'o', 'o', 'o'],
#     ['x', 'o', 'o', 'o', 'o']
# ])

# # Parameters for specific counts of A, B, and C
# num_a = 1  # Example number of A's
# num_b = 1  # Example number of B's
# num_c = 1  # Example number of C's

# # Step 1: Identify odd-indexed 'o' positions
# odd_positions = []
# for row in range(matrix.shape[0]):
#     for col in range(matrix.shape[1]):
#         if row % 2 == 1 and col % 2 and matrix[row, col] == 'o':
#             odd_positions.append((row, col))

# # Check if the number of required positions matches with counts of A, B, and C
# if len(odd_positions) < num_a + num_b + num_c:
#     print("Not enough odd 'o' positions to place all A, B, and C items.")
# else:
#     # Step 2: Generate the list of items to place
#     items = ['A'] * num_a + ['B'] * num_b + ['C'] * num_c

#     # Step 3: Generate all unique permutations of these items in the odd positions
#     unique_combinations = set(permutations(items))

#     # Step 4: Generate matrices for each unique combination
#     result_matrices = []
#     for combo in unique_combinations:
#         # Create a copy of the matrix to apply this combination
#         new_matrix = matrix.copy()
#         for pos, item in zip(odd_positions, combo):
#             new_matrix[pos] = item
#         result_matrices.append(new_matrix)

# # Display result
# for i, result in enumerate(result_matrices):
#     print(f"Combination {i+1}:\n{result}\n")
#     combinations = []
#     combinations.append(i)


############################
from itertools import permutations
from itertools import permutations, product
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
num_b = 0  # Example number of B's
num_c = 0  # Example number of C's

# Step 1: Identify odd-indexed 'o' positions
odd_positions = []
for row in range(matrix.shape[0]):
    for col in range(matrix.shape[1]):
        if row % 2 == 1 and col % 2 == 1 and matrix[row, col] == 'o':
            odd_positions.append((row, col))

# print(odd_positions)

# Check if the number of required positions matches with counts of A, B, and C
if len(odd_positions) < num_a + num_b + num_c:
    print("Not enough odd 'o' positions to place all A, B, and C items.")
else:
    # Step 2: Generate the list of items to place
    items = ['A'] * num_a + ['B'] * num_b + ['C'] * num_c

print(items)

# Step 3: Generate all unique permutations of these items in the odd positions
unique_combinations = set(permutations(items))

# Step 4: Store matrices for each unique combination in a list
result_matrices = []
for combo in unique_combinations:
    # Create a copy of the matrix to apply this combination
    new_matrix = matrix.copy()
    for pos, item in zip(odd_positions, combo):
        new_matrix[pos] = item
        result_matrices.append(new_matrix)

print(result_matrices)

# result_matrices now contains all the matrices with unique combinations of A, B, and C in odd positions

# Convert each matrix to a list of lists for a cleaner display
formatted_matrices = [matrix.tolist() for matrix in result_matrices]
# print(formatted_matrices)



