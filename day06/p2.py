
f = open("puzzle_input.txt", "r")
puzzle_input = f.read()
marker_size = 14

for i in range(len(puzzle_input)):
    word = puzzle_input[i:i+marker_size]
    if(len(set(word)) == marker_size):
        print(i + marker_size) # 3452
        break
    