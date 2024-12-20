from typing import List
from piece import Piece, Color
class Pawn(Piece):
    # def __init__(self, color: Color, current_pos: str): (inherited from Piece())

   
    # returns the non validated possible moves a piece can make
    def move(self) -> List[str]:
        # returns two available moves if pawns are in starting position
        for  char in self.cols:
            if self.color == Color.white and self.current_pos == f'{char}2':
                return self.move_forward(2)

            if self.color == Color.black and self.current_pos == f'{char}7':
                return self.move_forward(2)

        return self.move_forward(1)
        

    def take(self) -> tuple [ List[str], List[str] ]:
        return self.move_diagonally(1)
    


p_white_start = Pawn(Color.white, 'd2')
p_white_moved = Pawn(Color.white, 'd3')


p_black_start = Pawn(Color.black, 'd7')
p_black_moved = Pawn(Color.black, 'd6')

print('Pawn Tests  move() START --------------')
print(f'white start {p_white_start.current_pos}: ', p_white_start.move())
print(f'white moved {p_white_moved.current_pos}: ', p_white_moved.move())

print(f'black start {p_black_start.current_pos}: ', p_black_start.move())
print(f'p_black_moved {p_black_moved.current_pos}: ', p_black_moved.move())
print('Pawn Tests move() END --------------\n')


p_take = Pawn(Color.white, 'd4')
print('Pawn Tests take() START --------------')
print(f'origin: [ {p_take.current_pos} ]: ', p_take.take())
print('Pawn Tests take() END --------------\n')

