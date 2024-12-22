from pawn import Pawn
from queen import Queen
from knight import Knight
from rook import Rook
from bishop import Bishop
from king import King



class ChessBoard:


    def __init__(self, as_white = True):
        
            #The chess board is read as each sub array being a row on the chess board.
            #The start of the array is the side facing the user.
            #maybe change each of these numbers into piece classes
            #EVAN: Rook, Knight, Queen
            #Raul: Bishop, King, Pawn
            #
        self.pieceLocations = [[Rook("white",'a1'), Pawn("white",'b1'), None, None, None, None, Pawn("black",'g1'), Rook("black",'h1')],\
                            [Knight("white",'a2'), Pawn("white",'b2'), None, None, None, None, Pawn("black",'g2'), Knight("black",'h2')],\
                            [Bishop("white",'a3'), Pawn("white",'b3'), None, None, None, None, Pawn("black",'g3'), Bishop("black",'h3')],\
                            [Queen("white",'a4'), Pawn("white",'b4'), None, None, None, None, Pawn("black",'g4'), Queen("black",'h4')],\
                            [King("white",'a5'), Pawn("white",'b5'), None, None, None, None, Pawn("black",'g5'), King("black",'h5')],\
                            [Bishop("white",'a6'), Pawn("white",'b6'), None, None, None, None, Pawn("black",'g6'), Bishop("black",'h6')],\
                            [Knight("white",'a7'), Pawn("white",'b7'), None, None, None, None, Pawn("black",'g7'), Knight("black",'h7')],\
                            [Rook("black",'a8'), Pawn("white",'b8'), None, None, None, None, Pawn("black",'g8'), Rook("black",'h8')]]
        
        #we will represent the chessboard as a dictionary with each sqaure given
        #its proper letter and number as a key. its value will be the piece at that
        #square

        self.chessBoard = {}

        #the ASCII value for 'a' in python is 97. so subtract 97 to access index 0.

        for column in range(ord('a'), ord('h')+1):
            for row in range(1, 9):
                try:
                    self.pieceLocations[row-1][column-97].current_pos = f"{chr(column)}{row}"
                    self.chessBoard[f"{chr(column)}{row}"] = self.pieceLocations[row-1][column-97]
                except:
                    self.chessBoard[f"{chr(column)}{row}"] = None


     
    #def move(piece, prev_pos_row,prev_pos_column, new_pos_row, new_pos_column):
        #make a .get_type for each piece
        #self.chessBoard[]

chessboard = ChessBoard()
print(chessboard.pieceLocations)