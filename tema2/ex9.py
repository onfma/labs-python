# Write a function that receives as paramer a matrix which represents the heights 
# of the spectators in a stadium and will return a list of tuples (line, column) 
# each one representing a seat of a spectator which can't see the game.
# A spectator can't see the game if there is at least one taller spectator standing in front of him.
# All the seats are occupied. All the seats are at the same level. Row and column indexing starts from 0,
# beginning with the closest row from the field.

def find_obstructed_seats(matrix):
    obstructed_seats = []

    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows):
        for col in range(cols):
            height = matrix[row][col]

            obstructed = False
            for r in range(row + 1, rows):
                if matrix[r][col] > height:
                    obstructed = True
                    break

            if not obstructed:
                obstructed_seats.append((row, col))

    return obstructed_seats

# Example usage:
stadium = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]

obstructed = find_obstructed_seats(stadium)
print(obstructed)
