from game.visuals import visuals
from game.board import Board
from game.board import pawn_move


def main():
    board = Board()
    print(visuals(board))

    print("Which pawn will you move?")

    a, b = map(int, input().split())
    print("to where?")
    i, j = map(int, input().split())

    pawn_move(board, a, b, i, j)

    print(visuals(board))

    

if __name__ == "__main__":
    main()