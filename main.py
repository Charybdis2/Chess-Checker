# Chess Checker
# By Charybdis
#Naming conventions used: https://en.wikipedia.org/wiki/Forsyth–Edwards_Notation#cite_note-pgn_spec-1
#Used, k - king, q - Queen, b - Bishop, r - rook, p - pawn, n - knight. Captionals denote white pieces lowercase black

def read_file(file_name):
    #This function reads the file given and calls board_check()
    count = 0
    board = []
    file = open(file_name , 'r')
    for line in file:
        if len(line)<8:
            count = count+1
            print("Game #", count, board_check(board))
            board = []
        else:
            board.append(line)
        
def find_piece(board, piece):
    #This can be used to find any piece, but is used to find the king
    for c in range(8):
        for r in range(8):
            if board[r][c] == piece:
                return r,c

def get_piece(board, r, c):
    #to make sure the code doesn't break if it tries to check if there is a knight or any piece off the board
    if r < 0 or r >7 or c > 7 or c < 0:
        return "."
    return board[r][c]

def check_pawn(board, kr, kc, p, iswhite):
    #Checks if a pawn can take the king
    
    if get_piece(board, kr+iswhite, kc+1) == p:
        return True
    if get_piece(board, kr+iswhite, kc-1) == p:
        return True
    return False


def check_knight(board, kr, kc, n):
    #Checks if a Knight can take the king 
    for ro, co in [(1,2), (-1,2), (1,-2), (-1,-2), (2,1), (-2,1), (2,-1), (-2,-1)]:
        if get_piece(board, kr+ro, kc+co) == n:
            return True
    return False

def check_rowcolumn(board, kr, kc):
    #Checks the whole row & column if there is a queen, rook or if a piece is blocking it
    for ro, co in [(1,0), (0,1), (-1,0), (0,-1)]:
        r = kr
        c = kc
        while r >= 0 and r <=7 and c>=0 and c<=7:
            r = r+ro
            c = c+co
            piece = get_piece(board, r, c)
            if piece == "Q" or piece == "R":
                 return True
            if piece != ".":
                break
    return False

def check_diagonal(board, kr, kc):
    #Checks the whole row & column if there is a queen, bishop or if a piece is blocking it
    for ro, co in [(1,1), (-1,1), (-1,-1), (1,-1)]:
        r = kr
        c = kc
        while r >= 0 and r <=7 and c>=0 and c<=7:
            r = r+ro
            c = c+co
            piece = get_piece(board, r, c)
            if piece == "Q" or piece == "B":
                 return True
            if piece != ".":
                break
    return False
def check_rowcolumnW(board, kr, kc):
    for ro, co in [(1,0), (0,1), (-1,0), (0,-1)]:
        r = kr
        c = kc
        while r >= 0 and r <=7 and c>=0 and c<=7:
            r = r+ro
            c = c+co
            piece = get_piece(board, r, c)
            if piece == "q" or piece == "r":
                 return True
            if piece != ".":
                break
    return False

def check_diagonalW(board, kr, kc):
    for ro, co in [(1,1), (-1,1), (-1,-1), (1,-1)]:
        r = kr
        c = kc
        while r >= 0 and r <=7 and c>=0 and c<=7:
            r = r+ro
            c = c+co
            piece = get_piece(board, r, c)
            if piece == "q" or piece == "b":
                 return True
            if piece != ".":
                break
    return False

def board_check(board):
    #Checks if there is a king or not, so the code doesn't break
    location = find_piece(board, "k")
    if location is None:
        return "Finished"
    kr, kc = location
    if check_pawn(board, kr, kc, "P", +1):
        return "Black king is in check"
    if check_knight(board, kr,kc, "N"):
        return "Black king is in check"
    if check_rowcolumn(board, kr, kc):
        return "Black king is in check"
    if check_diagonal(board, kr, kc):
        return "Black king is in check"
    Kr, Kc = find_piece(board, "K")
    if check_pawn(board, Kr, Kc, "p", -1):
        return "White king is in check"
    if check_knight(board, Kr,Kc, "n"):
        return "White king is in check"
    if check_rowcolumnW(board, Kr, Kc):
        return "White king is in check"
    if check_diagonalW(board, Kr, Kc):
        return "White king is in check"
    return "No King is in check"



#The actual code.
read_file("boardone.txt")

    
        
        
    

