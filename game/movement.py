from game.pieces import Piece


def pawn_movement(board, i, j):
    
    if board.squares[i][j].type == "Pawn":
        board.squares[i][j] = None
        board.squares[i-1][j] = Piece("White", "Pawn")