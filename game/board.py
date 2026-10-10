from game.pieces import Piece
from game.rules import all_legal_moves

class Board:
    def __init__(self):
        self.turn = "White"
        self.squares = [[None for i in range(8)] for i in range(8)]
        self.starting_position()
    def starting_position(self):
        back_rank = ["Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook"]
        for i in range(8):
            self.squares[0][i] = Piece("Black", back_rank[i])
        for i in range(8):
            self.squares[7][i] = Piece("White", back_rank[i])
        self.squares[1] = [Piece("Black", "Pawn") for i in range(8)]
        self.squares[6] = [Piece("White", "Pawn") for i in range(8)]




def move(board, start: tuple, end: tuple):
    a, b = start
    c, d = end

    if board.squares[a][b] is not None:
        if board.turn == board.squares[a][b].color:
           
            if ((start, end) in all_legal_moves(board, board.squares[a][b].color)):
                board.squares[c][d] = board.squares[a][b]
                board.squares[a][b] = None
                board.squares[c][d].has_moved = True
                if board.turn == "White":
                    board.turn = "Black"
                else:
                    board.turn = "White" 
            else:
                print("Illegal move")
        else:
            print("Not your turn")
    else:
        print("No piece on that square")
