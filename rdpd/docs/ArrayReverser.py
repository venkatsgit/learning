class ArrayReverser:
    def __init__(self, array):
        self.array = array

    def reverser(self):
        if len(self.array) > 0:
            left = 0
            right = len(self.array) - 1
            while left < right:
               self.array[left] ,self.array[right] = self.array[right], self.array[left]
               left += 1
               right -= 1



def reconstruct_binary_matrix(row_sums, col_sums):
    # Check if reconstruction is possible
    if sum(row_sums) != sum(col_sums):
        return None  # Impossible to reconstruct
    
    # Initialize the matrix
    rows = len(row_sums)
    cols = len(col_sums)
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # First pass: Try to place 1s based on row and column constraints
    for i in range(rows):
        for j in range(cols):
            # If placing 1 doesn't exceed row or column sum, place it
            if (row_sums[i] > 0 and col_sums[j] > 0):
                matrix[i][j] = 1
                row_sums[i] -= 1
                col_sums[j] -= 1
    
    # Verify if we've satisfied all constraints
    if all(r == 0 for r in row_sums) and all(c == 0 for c in col_sums):
        return matrix
    
    return None  # Unable to reconstruct

# Example usage
def print_matrix(matrix):
    if matrix is None:
        print("No solution exists")
    else:
        for row in matrix:
            print(row)

# Example 1: Possible reconstruction
row_sums1 = [3, 2]  # First row needs 3 ones, second row needs 2 ones
col_sums1 = [2, 2, 1]  # First column has 2 ones, second column has 2 ones, third column has 1 one
print("Example 1:")
print_matrix(reconstruct_binary_matrix(row_sums1, col_sums1))

# Example 2: Impossible reconstruction
row_sums2 = [4, 3]
col_sums2 = [2, 2, 3]
print("\nExample 2:")
print_matrix(reconstruct_binary_matrix(row_sums2, col_sums2))

def create_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        # Create a row of zeros
        row = [0] * cols
        matrix.append(row)
    return matrix

# Example usage
matrix = create_matrix(3, 4)
print(matrix)
