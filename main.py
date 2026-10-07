from game.visuals import visuals
from game.board import Board
from game.movement import pawn_movement

def main():
    board = Board()
    print(visuals(board))


    print("Which white pawn will you move? 1-8")

    move = int(input())

    pawn_movement(board, 6, move-1)

    print(visuals(board))

    

if __name__ == "__main__":
    main()