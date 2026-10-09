from game.movement import pawn_legal_attacks
from game.movement import knight_legal_moves
from game.movement import bishop_legal_moves
from game.movement import queen_legal_moves
from game.movement import king_legal_moves
from game.movement import rook_legal_moves
from game.movement import king_legal_moves

def is_king_in_check(board, color):
    for i in range(8):
        for j in range(8):
            if board.squares[i][j] is not None:
                if board.squares[i][j].type == "King" and board.squares[i][j].color == color:
                    king_pos = (i, j)


    pieces_movement = {
        "Pawn": pawn_legal_attacks,
        "Rook": rook_legal_moves,
        "Bishop": bishop_legal_moves,
        "Queen": queen_legal_moves,
        "King": king_legal_moves,
        "Knight": knight_legal_moves}
    
    for i in range(8):
        for j in range(8):
            if board.squares[i][j] is not None:
                if board.squares[i][j].color != color:
                    for p, m in pieces_movement.items():
                        if board.squares[i][j].type == p:
                            legal_moves = m(board, i, j)
                            if king_pos in legal_moves:
                                return True

    return False
    
        
                    