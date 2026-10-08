from game.pieces import Piece


def pawn_legal_moves(board, i, j):
    legal_moves = []

    if board.squares[i][j] != None:
        if board.squares[i][j].type == "Pawn":
            if board.squares[i][j].color == "White":
                if i == 6:
                    if board.squares[i-2][j] == None and board.squares[i-1][j] == None:
                        legal_moves.append((i-2, j))

                if i > 0 and board.squares[i-1][j] == None:
                    legal_moves.append((i-1, j))

                if j>0 and board.squares[i-1][j-1] != None and board.squares[i-1][j-1].color == "Black" :
                    legal_moves.append((i-1, j-1))
                if j<7 and board.squares[i-1][j+1] != None and board.squares[i-1][j+1].color == "Black":
                    legal_moves.append((i-1, j+1))
                    
            else:
                if i == 1:
                    if board.squares[i+2][j] == None and board.squares[i+1][j] == None:
                        legal_moves.append((i+2,j))
                
                if board.squares[i+1][j] == None:
                    legal_moves.append((i+1,j))
                
                if j>0 and board.squares[i+1][j-1] != None and board.squares[i+1][j-1].color == "White" :
                    legal_moves.append((i+1,j-1))
                if j<7 and board.squares[i+1][j+1] != None and board.squares[i+1][j+1].color == "White" :
                    legal_moves.append((i+1,j+1))

    return(legal_moves)

def rook_legal_moves(board, i, j):
    legal_moves = []

    if board.squares[i][j] != None:
        if board.squares[i][j].type == "Rook":
            color = board.squares[i][j].color

            
            for r in range(i-1, -1, -1):
                if board.squares[r][j] == None:
                    legal_moves.append((r, j))
                elif board.squares[r][j].color != color:
                    legal_moves.append((r, j))
                    break
                else:
                    break

            for r in range(i+1, 8): 
                if board.squares[r][j] == None:
                    legal_moves.append((r, j))
                elif board.squares[r][j].color != color:
                    legal_moves.append((r, j))
                    break
                else:
                    break
            for c in range(j-1, -1, -1):
                if board.squares[i][c] == None:
                    legal_moves.append((i, c))
                elif board.squares[i][c].color != color:
                    legal_moves.append((i, c))
                    break
                else:
                    break
            for c in range(j+1, 8):
                if board.squares[i][c] == None:
                    legal_moves.append((i, c))
                elif board.squares[i][c].color != color:
                    legal_moves.append((i, c))
                    break
                else:
                    break

    return(legal_moves)

def bishop_legal_moves(board, i, j):
    legal_moves = []
    if board.squares[i][j] != None:
        if board.squares[i][j].type == "Bishop":
            color = board.squares[i][j].color 
            for l, r in zip(range(i-1, -1, -1,), range(j-1, -1, -1)):
                if board.squares[l][r] == None:
                    legal_moves.append((l, r))
                elif board.squares[l][r].color != color:
                    legal_moves.append((l, r))
                    break
                else:
                    break
            for l, r in zip(range(i-1, -1, -1), range(j+1, 8)):
                if board.squares[l][r] == None:
                    legal_moves.append((l, r))
                elif board.squares[l][r].color != color:
                    legal_moves.append((l, r))
                    break
                else:
                    break
            for l, r in zip(range(i+1, 8), range(j-1, -1, -1)):
                if board.squares[l][r] == None:
                    legal_moves.append((l, r))
                elif board.squares[l][r].color != color:
                    legal_moves.append((l, r))
                    break
                else:
                    break
            for l, r in zip(range(i+1, 8), range(j+1, 8)):
                if board.squares[l][r] == None:
                    legal_moves.append((l, r))
                elif board.squares[l][r].color != color:
                    legal_moves.append((l, r))
                    break
                else:
                    break
    return(legal_moves)
            
