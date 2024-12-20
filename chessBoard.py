from pawn import Pawn
from queen import Queen
from knight import Knight
from rook import Rook
#from king import King
#from bishop import Bishop


class ChessBoard:


    def __init__(self, as_white = True):
        
            #The chess board is read as each sub array being a row on the chess board.
            #The start of the array is the side facing the user.
            #maybe change each of these numbers into piece classes
            #EVAN: Rook, Knight, Queen
            #Raul: Bishop, King, Pawn
            #
        self.pieceLocations = [[Rook("white"), Pawn("white"), None, None, None, None, Pawn("black"), Rook("black")],\
                            [Knight("white"), Pawn("white"), None, None, None, None, Pawn("black"), Knight("black")],\
                            [Bishop("white"), Pawn("white"), None, None, None, None, Pawn("black"), Bishop("black")],\
                            [Queen("white"), Pawn("white"), None, None, None, None, Pawn("black"), Queen("black")],\
                            [King("white"), Pawn("white"), None, None, None, None, Pawn("black"), King("black")],\
                            [Bishop("white"), Pawn("white"), None, None, None, None, Pawn("black"), Bishop("black")],\
                            [Knight("white"), Pawn("white"), None, None, None, None, Pawn("black"), Knight("black")],\
                            [Rook("black"), Pawn("white"), None, None, None, None, Pawn("black"), Rook("black")]]
        
        #we will represent the chessboard as a dictionary with each sqaure given
        #its proper letter and number as a key. its value will be the piece at that
        #square

        self.chessBoard = {}

        #the ASCII value for 'a' in python is 97. so subtract 97 to access index 0.

        for column in range(ord('a'), ord('h')+1):
            for row in range(1, 9):
                self.pieceLocations[row-1][column-97].current_pos = f"{chr(column)}{row}"
                self.chessBoard[f"{chr(column)}{row}"] = self.pieceLocations[row-1][column-97]


        
    #def move(piece, prev_pos_row,prev_pos_column, new_pos_row, new_pos_column):
        #make a .get_type for each piece
        #self.chessBoard[]

     