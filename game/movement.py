from game.pieces import Piece


def pawn_legal_moves(board, i, j):
    legal_moves = []

    if board.squares[i][j] != None:
        if board.squares[i][j].type == "Pawn":
            if board.squares[i][j].color == "White":
                if i == 6:
                    if board.squares[i-2][j] == None and board.squares[i-1][j] == None:
                        legal_moves.append((i-2, j))

                if board.squares[i-1][j] == None:
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
