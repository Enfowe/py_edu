start_pos = input("Enter cells: ")
cells = [[start_pos[0], start_pos[1], start_pos[2]],
         [start_pos[3], start_pos[4], start_pos[5]],
         [start_pos[6], start_pos[7], start_pos[8]]]

с = """[[0, 1, 2],
         [3, 4, 5],
         [6, 7, 8],
         [0, 3, 6],
         [1, 4, 7],
         [2, 5, 8],
         [0, 4, 8],
         [2, 4, 6]]"""
        
moves = {(1, 3): cells[0][0], (2, 3): cells[0][1], (3, 3): cells[0][2],
         (1, 2): cells[1][0], (2, 2): cells[1][1], (3, 2): cells[1][2],
         (1, 1): cells[2][0], (2, 1): cells[2][1], (3, 1): cells[2][2]}


def print_field():
    print(f"""---------
| {moves[(1,3)]} {moves[(2,3)]} {moves[(3,3)]} |
| {moves[(1,2)]} {moves[(2,2)]} {moves[(3,2)]} |
| {moves[(1,1)]} {moves[(2,1)]} {moves[(3,1)]} |
---------""")

print_field()
input_ = True
while input_:
    try:
        move = tuple([int(num) for num in input().split()])
    except:
        print("You should enter numbers!") 
        continue
    if move not in moves:
        print("Coordinates should be from 1 to 3!")
        continue
    if moves[move] != "_":
        print("This cell is occupied! Choose another one!")
        continue
    moves[move] = "X"
    input_ = False
print_field()
