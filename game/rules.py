from game.movement import pawn_legal_attacks
from game.movement import knight_legal_moves
from game.movement import bishop_legal_moves
from game.movement import queen_legal_moves
from game.movement import king_legal_moves
from game.movement import rook_legal_moves
from game.movement import king_legal_moves
from game.movement import pawn_legal_moves
from game.pieces import Piece



def is_square_attacked(board, color, square):
    i, j = square

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
                            if square in legal_moves:
                                return True

    return False

def is_king_in_check(board, color):
    for i in range(8):
        for j in range(8):
            if board.squares[i][j] is not None and board.squares[i][j].color == color and board.squares[i][j].type == "King":
                return is_square_attacked(board, color, (i, j))

def all_legal_moves(board, color):
    pieces_movement = {
        "Pawn": pawn_legal_moves,
        "Rook": rook_legal_moves,
        "Bishop": bishop_legal_moves,
        "Queen": queen_legal_moves,
        "King": king_legal_moves,
        "Knight": knight_legal_moves}
    legal_moves = []
    curr_pieces = []
    
    for i in range(8):
        for j in range(8):
            if board.squares[i][j] is not None and board.squares[i][j].color == color:
                curr_pieces.append((i, j))

    for piece in curr_pieces:
        i, j = piece
        for moves in pieces_movement[board.squares[i][j].type](board, i, j):
            a, b = moves
            captured_piece = board.squares[a][b]
            board.squares[a][b] = board.squares[i][j]
            board.squares[i][j] = None
            
            if not is_king_in_check(board, color):
                legal_moves.append(((i,j),moves))
            
            
            board.squares[i][j] = board.squares[a][b]
            board.squares[a][b] = captured_piece
    return(legal_moves)



def checkmate_stalemate(board, color):
    
    if all_legal_moves(board, color) == []:
        if is_king_in_check(board, color):
            print("Checkmate")
        else:
            print("Stalemate")
    return

def pawn_promotion(board, square):
    i, j = square
    color = ""
    piece_promotion = {
        "q": Piece(color, "Queen"),
        "n": Piece(color, "Knight"),
        "b": Piece(color, "Bishop"),
        "r": Piece(color, "Rook")

    }
    if board.squares[i][j] != None:
        if board.squares[i][j].type == "Pawn":
            if board.squares[i][j].color == "White":
                color = "White"
                if i == 0:
                    print("What piece will your pawn promote to (please enter a letter)")
                    user_piece = input()
                    board.squares[i][j] = piece_promotion[user_piece]
            elif board.squares[i][j].color == "Black":
                color = "Black"
                if i == 7:
                    print("What piece will your pawn promote to (please enter a letter)")
                    user_piece = input()
                    board.squares[i][j] = piece_promotion[user_piece]

