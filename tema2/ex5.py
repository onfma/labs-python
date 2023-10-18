# Write a function that receives as parameter a matrix and will return 
# the matrix obtained by replacing all the elements under the main diagonal with 0 (zero).

def replace_below_diagonal_with_zero(matrix):
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if i > j:
                matrix[i][j] = 0

    return matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = replace_below_diagonal_with_zero(matrix)

for row in result:
    print(row)
