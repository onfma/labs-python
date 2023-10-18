# Write a function that receives as a parameters a list of musical notes (strings), 
# a list of moves (integers) and a start position (integer). 
# The function will return the song composed by going though the musical notes 
# beginning with the start position and following the moves given as parameter.
# Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"] 

def compose(notes, moves, start_position):
    song = []
    current_position = start_position

    for move in moves:
        current_position = (current_position + move) % len(notes)
        song.append(notes[current_position])

    return song

notes = ["do", "re", "mi", "fa", "sol"]
moves = [1, -3, 4, 2]
start_position = 2
print(compose(notes, moves, start_position))
