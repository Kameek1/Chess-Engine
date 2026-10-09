from game.board import Board

def visuals(B):
    symbols = {

        "Pawn": "P",
        "Queen":"Q",
        "King": "K",
        "Bishop":"B",
        "Rook": "R",
        "Knight":"N"
    }

    rows = []

    for i in B.squares:
        cells = []
        for j in i:
            if j == None:
                cells.append(".")
            else:
                symbol = symbols[j.type]
                if j.color == "Black":
                    symbol = symbol.lower()
                cells.append(symbol)

        
        rows.append(" ".join(cells))


    return("\n".join(rows))

def square_name(square:str):
    col = ord(square[0]) - ord("a")
    row = 8 - int(square[1])

    return (row, col)