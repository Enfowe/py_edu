cells = input("Enter cells: ")
print("""---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------""".format(*cells))
combs = ([0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6])
        

def states():
    x_win = None
    o_win = None
    impossible = None
    empty = None
    draw = None
    
    if "_" in cells or " " in cells:
        empty = True
    else:
        empty = False

    for comb in combs:
        f, s, t = comb
        if cells[f] == cells[s] == cells[t]:
            if cells[f] == "X":
                x_win = True
            if cells[f] == "O":
                o_win = True
    
    impossible = o_win and x_win
    draw = not o_win and not x_win and not empty
    game_over = not empty
    return (x_win, o_win, impossible, draw, game_over)
    
x_win, o_win, impossible, draw, game_over = states()        

if abs(cells.count("X") - cells.count("O")) > 1 or impossible:
    print("Impossible")
elif draw:
    print("Draw")
elif x_win:
    print("X wins")
elif o_win:
    print("O wins")
else:
    print("Game not finished")
    
