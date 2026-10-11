from game.board import Board
from game.rules import all_legal_moves
from game.pieces import Piece
def test_castle():
    board = Board()
    for i in range(8):
        for j in range(8):
            board.squares[i][j] = None
    board.squares[7][4] = Piece("White", "King")
    board.squares[7][0] = Piece("White", "Rook")
    board.squares[7][4] = Piece("White", "Rook")

    moves = all_legal_moves(board, "Black")

    assert((7, 4),(7, 2)) in moves
    assert((7, 4),(7, 6)) in moves