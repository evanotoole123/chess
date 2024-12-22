from chessBoard import ChessBoard
from pawn import Pawn
from rook import Rook
from knight import Knight
from queen import Queen
from bishop import Bishop
from king import King
from typing import List
from piece import Color

'''

p_white_start = Pawn(Color.white, 'd2')
p_white_moved = Pawn(Color.white, 'd3')


p_black_start = Pawn(Color.black, 'c6')
p_black_moved = Pawn(Color.black, 'd6')

print(p_black_start.get_unvalidated_moves())
#print(p_black_moved.get_unvalidated_moves())

'''

'''
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

'''

print('TESTING KNIGHT-----------')
knight = Knight('white', 'd4')
print(knight.move('b5'))


print('TESTING QUEEN--------')
queen = Queen('white', 'd4')
print(queen.move('a1'))
print(queen.move('h8'))


print('TESTING KING--------')
king = King('white', 'e4')
print(king.move('e5'))
king2 = King('white', 'a1')
print(king2.move('b2'))


print('TESTING BISHOP--------')
bishop = Bishop('white', 'c4')
print(bishop.move('b3'))
print(bishop.move('g8'))