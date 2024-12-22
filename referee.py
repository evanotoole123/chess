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
        pass

    #when a piece takes another just replace one piece with the other, and change
    def take_square(self,):
        pass


    #returns all possible lines/paths for a given piece
    def find_reachable_squares(self, piece: object) -> List[List[str]]:
        unvalidated_moves: List[List[str]] = piece.get_unvalidated_moves()
        