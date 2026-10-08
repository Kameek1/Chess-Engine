from game.visuals import visuals
from game.board import Board
from game.board import move

def user_input():
    print("Which piece will you move?")
    piece = tuple(map(int, input().split()))
    print("where will you move it")
    move = tuple(map(int, input().split()))

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




