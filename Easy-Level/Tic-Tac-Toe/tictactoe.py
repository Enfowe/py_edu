# JetBrains Academy
# Project: Tic Tac Toe
# Stage 5/5

moves = {(1, 3): "_", (2, 3): "_", (3, 3): "_",
         (1, 2): "_", (2, 2): "_", (3, 2): "_",
         (1, 1): "_", (2, 1): "_", (3, 1): "_"}


def update_combs():
    global combs
    combs = [[moves[1, 3], moves[2, 3], moves[3, 3]],
             [moves[1, 2], moves[2, 2], moves[3, 2]],
             [moves[1, 1], moves[2, 1], moves[3, 1]],
             [moves[1, 3], moves[1, 2], moves[1, 1]],
             [moves[2, 3], moves[2, 2], moves[2, 1]],
             [moves[3, 3], moves[3, 2], moves[3, 1]],
             [moves[1, 3], moves[2, 2], moves[3, 1]],
             [moves[1, 1], moves[2, 2], moves[3, 3]]]


def print_field():
    print(f"""---------
| {moves[(1, 3)]} {moves[(2, 3)]} {moves[(3, 3)]} |
| {moves[(1, 2)]} {moves[(2, 2)]} {moves[(3, 2)]} |
| {moves[(1, 1)]} {moves[(2, 1)]} {moves[(3, 1)]} |
---------""")


print_field()


def states():
    o_win = None
    x_win = None
    
    if "_" in moves.values():
        empty = True
    else:
        empty = False

    for comb in combs:
        first, second, third = comb
        if first == second == third:
            if first == "X":
                x_win = True
            if first == "O":
                o_win = True

    impossible = o_win and x_win
    draw = not o_win and not x_win and not empty
    game_over = not empty
    return (x_win, o_win, impossible, draw, game_over)


current_char = "X"
prev_char = "O"
input_ = True
while input_:
    try:
        print("Enter the coordinates: ")
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
    moves[move] = current_char
    current_char, prev_char = prev_char, current_char

    print_field()

    update_combs()
    x_win, o_win, impossible, draw, game_over = states()

    if impossible:
        print("Impossible")
        input_ = False
    elif draw:
        print("Draw")
        input_ = False
    elif x_win:
        print("X wins")
        input_ = False
    elif o_win:
        print("O wins")
        input_ = False
    else:
        continue
