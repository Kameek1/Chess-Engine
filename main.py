from game.visuals import visuals
from game.board import Board
from game.board import move
from game.visuals import square_name



def user_input():
    print("Which piece will you move?")
    piece = square_name(input())
    
    print("where will you move it")
    move = square_name(input())

    return((piece, move))

def main():
    board = Board()
    print(visuals(board))

    for i in range(100):
        start, end = user_input()

        move(board, start, end)
        print(visuals(board))




if __name__ == "__main__":
    main()




