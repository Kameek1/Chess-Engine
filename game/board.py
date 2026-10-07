from game.pieces import Piece
from game.movement import pawn_legal_moves

class Board:
    def __init__(self):
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

def pawn_move(board, a, b, i, j):
    legal_moves = pawn_legal_moves(board, a, b)
    if (i, j) in legal_moves:
        board.squares[i][j] = Piece(board.squares[a][b].type, "Pawn")
        board.squares[a][b] = None
        

    else:
        return("This is not a legal move")



