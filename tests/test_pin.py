from game.board import Board
from game.rules import all_legal_moves
from game.pieces import Piece
def test_rook_pin():
    board = Board()
    for i in range(8):
        for j in range(8):
            board.squares[i][j] = None
    board.squares[0][0] = Piece("White", "Rook")
    board.squares[0][2] = Piece("Black", "Rook")
    board.squares[0][4] = Piece("Black", "King")

    moves = all_legal_moves(board, "Black")

    assert((0, 2),(1, 2)) not in moves