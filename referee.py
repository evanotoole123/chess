from chessBoard import ChessBoard
from pawn import Pawn
from rook import Rook
from knight import Knight
from queen import Queen
from bishop import Bishop
from typing import List


class Referee:
    def __init__(self):
        self.chessboard_dct = ChessBoard()
        self.white_check = False
        self.black_check = False
    
    def validate_move(self, move: List[str])->bool:
        
    def swap_squares(self):

    def take_square(self,):