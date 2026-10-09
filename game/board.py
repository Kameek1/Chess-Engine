from game.pieces import Piece
from game.movement import pawn_legal_moves
from game.movement import queen_legal_moves
from game.movement import bishop_legal_moves
from game.movement import rook_legal_moves
from game.movement import king_legal_moves
from game.movement import knight_legal_moves
from game.movement import pawn_legal_attacks
from game.rules import is_king_in_check
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




def move(board, start: tuple, end: tuple):
    a, b = start
    c, d = end


    if board.squares[a][b].type == "Pawn":
        if (c, d) in pawn_legal_moves(board, a, b):
            board.squares[c][d] = board.squares[a][b]
            board.squares[a][b] = None
        elif (c, d) in pawn_legal_attacks(board, a, b):
            board.squares[c][d] = board.squares[a][b]
            board.squares[a][b] = None
    elif board.squares[a][b].type == "Rook":
        if (c, d) in rook_legal_moves(board, a, b):
            board.squares[c][d] = board.squares[a][b]
            board.squares[a][b] = None
    elif board.squares[a][b].type == "Bishop":
        if (c, d) in bishop_legal_moves(board, a, b):
            board.squares[c][d] = board.squares[a][b]
            board.squares[a][b] = None
    elif board.squares[a][b].type == "Queen":
        if (c, d) in queen_legal_moves(board, a, b):
            board.squares[c][d] = board.squares[a][b]
            board.squares[a][b] = None
    elif board.squares[a][b].type == "King":
        if (c, d) in king_legal_moves(board, a, b):
            board.squares[c][d] = board.squares[a][b]
            board.squares[a][b] = None
    elif board.squares[a][b].type == "Knight":
        if (c, d) in knight_legal_moves(board, a, b):
            board.squares[c][d] = board.squares[a][b]
            board.squares[a][b] = None
    else:
        print("This is an invalid move")
        return

    if is_king_in_check(board, board.squares[c][d].color):
        board.squares[a][b] = board.squares[c][d]
        board.squares[c][d] = None
        print("This leaves the king in check")