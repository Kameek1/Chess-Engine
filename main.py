from game.visuals import visuals
from game.board import Board
from game.movement import pawn_legal_moves


def main():
    board = Board()
    print(visuals(board))



    

if __name__ == "__main__":
    main()