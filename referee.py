from chessBoard import ChessBoard
from pawn import Pawn
from piece import Piece
from rook import Rook
from knight import Knight
from queen import Queen
from bishop import Bishop
from king import King
from typing import List


class Referee:
    def __init__(self, white_check = False, black_check = False):
        self.chessboard_dict = ChessBoard().chessBoard
        self.white_check = white_check
        self.taken_by_white = []

        self.black_check = black_check
        self.taken_by_black = []

    
    def validate_move(self, move: List[str])->bool:
        pass

    #when a piece takes another just replace one piece with the other, and change
    def take_square(self, piece: Piece, square: str):
        pass

    #returns all possible lines/paths for a given piece
    def find_reachable_squares(self, piece: Piece) -> List[str]:
        unvalidated_moves: List[List[str]] = piece.get_unvalidated_moves()
        reachable_squares = []
    
        for line in unvalidated_moves:
            reachable_squares.extend(self.find_longest_sequence(line, piece))
        return reachable_squares
            
           
    def find_longest_sequence(self, line: List[str], piece: Piece) -> List[str]:
        reachable_line = []
        
        for square in line:
            if(self.chessboard_dict[square] == None):
                reachable_line.append(square)
            elif self.chessboard_dict[square].color != piece.color and type(piece) != Pawn:
                reachable_line.append(square)
                break
            elif self.chessboard_dict[square].color != piece.color:
                if piece.current_pos[0] != square[0]:
                    reachable_line.append(square)
                break
            else:
                break
        
        return reachable_line

    def move(self, curr_pos: str, new_pos: str):

            curr_piece = self.chessboard_dict[ curr_pos ]
            taken_piece = self.chessboard_dict[ new_pos ]
            valid_moves = self.find_reachable_squares(curr_piece)

            # remove opponent piece and add it to list of taken pieces
            if isinstance(taken_piece, Piece): 
                if curr_piece.color == 'white':
                    self.taken_by_white.append(taken_piece)
                else:
                    self.taken_by_black.append(taken_piece)

            # update gameboard with moved piece
            if new_pos in valid_moves:
                self.chessboard_dict[ curr_piece.current_pos ] = None
                self.chessboard_dict[ new_pos ] = curr_piece 
                curr_piece.current_pos = new_pos

            #will remove this, just want to make sure pieces are moved correctly
            return curr_piece

    
    

print('BEGIN TESTING REFEREE ------------REACHABLE SQUARES')
print('testing starting points in chessboard: only pawns and knights can move')
ref = Referee()
print('TESTING ALL WHITE in initial position')
for i in range(ord('a'), ord('h')+1):
    print(ref.chessboard_dict[f'{chr(i)}2'])
    print(ref.find_reachable_squares(ref.chessboard_dict[f'{chr(i)}2']))
    print(ref.chessboard_dict[f'{chr(i)}1'])
    print(ref.find_reachable_squares(ref.chessboard_dict[f'{chr(i)}1']))
print('TESTING ALL BLACK in initial position')
for i in range(ord('a'), ord('h')+1):
    print(ref.chessboard_dict[f'{chr(i)}7'])
    print(ref.find_reachable_squares(ref.chessboard_dict[f'{chr(i)}7']))
    print(ref.chessboard_dict[f'{chr(i)}8'])
    print(ref.find_reachable_squares(ref.chessboard_dict[f'{chr(i)}8']))
print('testing pawn edge case')
print(ref.find_reachable_squares(Pawn('white', 'a6')))

print('MOVING PAWN')
ref.move('a2', 'a4')
ref.move('a4', 'a5')
ref.move('a5', 'a6')
ref.move('a6', 'b7')
print(ref.taken_by_white)

