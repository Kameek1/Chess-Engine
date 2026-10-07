from game.pieces import Piece


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


