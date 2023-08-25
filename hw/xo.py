import re

board = list(range(1,10))
win_combinations = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)]


def draw_board(ml):
    
    for i in range(3):
        print("--------------")
        print("|", board[i*3], "|", board[1 + i*3], "|", board[2 + i*3], "|")

def input_xo_place(player):
    while True:
        value = input("Place for player " + player + " ")
        if not value in "1,2,3,4,5,6,7,8,9":
            print("Write another number in range 1-9")
            continue 
        value = int(value)

        if str(board[value-1]) in "xo":
            print("This place is not free: Enter another number")
            continue
        board[value - 1] = player
        break

def iswin():
    for el in win_combinations:
        if board[el[0] - 1] == board[el[1] - 1] == board[el[2] - 1]:
            return board[el[0] - 1]
    return False
        
   
    

def main():
    counter = 0
    while True:
        draw_board(board)
        if counter % 2 == 0:
            input_xo_place("x")
        else:
            input_xo_place("o")
        
        if counter > 3:
            winner = iswin()
            if winner:
                draw_board(board)
                print("The winer is ", winner)
                break
        counter += 1
        if counter > 8 :
            print("Draw in the game")
            break
        

main()