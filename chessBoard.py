WHITE_PAWN = 1
BLACK_PAWN = 7

class ChessBoard:
    #1 = pawn_white
    #2 = bishop_white
    #3 = knight_white
    #4 = rook_white
    #5 = queen_white
    #6 = rook_white
    #7 = pawn_black
    #8 = bishop_black
    #9 = knight_black
    #10 = rook_black
    #11 = queen_black
    #12 = king_black





    def __init__(self):
        self.chessBoard = [[]]
        for i in range(7):
            self.chessBoard.append(0)
            for j in range(7):
                if j == 1:
                    self.chessBoard.append(BLACK_PAWN)
                if j == 6:
                    self.chessBoard.append(WHITE_PAWN)
                    
                self.chessBoard[i].append(0)
    
    def move(piece, prev_pos_row,prev_pos_column, new_pos_row, new_pos_column):
        #make a .get_type for each piece
        #self.chessBoard[]