from enum import Enum
from typing import List

class Color(Enum):
    white = 'white'
    black = 'black'

class Position(Enum):
    A1 = 'a1'
    A2 = 'a2'
    A3 = 'a3'
    A4 = 'a4'
    A5 = 'a5'
    A6 = 'a6'
    A7 = 'a7'
    A8 = 'a8'
    B1 = 'b1'
    B2 = 'b2'
    B3 = 'b3'
    B4 = 'b4'
    B5 = 'b5'
    B6 = 'b6'
    B7 = 'b7'
    B8 = 'b8'
    C1 = 'c1'
    C2 = 'c2'
    C3 = 'c3'
    C4 = 'c4'
    C5 = 'c5'
    C6 = 'c6'
    C7 = 'c7'
    C8 = 'c8'
    D1 = 'd1'
    D2 = 'd2'
    D3 = 'd3'
    D4 = 'd4'
    D5 = 'd5'
    D6 = 'd6'
    D7 = 'd7'
    D8 = 'd8'
    E1 = 'e1'
    E2 = 'e2'
    E3 = 'e3'
    E4 = 'e4'
    E5 = 'e5'
    E6 = 'e6'
    E7 = 'e7'
    E8 = 'e8'
    F1 = 'f1'
    F2 = 'f2'
    F3 = 'f3'
    F4 = 'f4'
    F5 = 'f5'
    F6 = 'f6'
    F7 = 'f7'
    F8 = 'f8'
    G1 = 'g1'
    G2 = 'g2'
    G3 = 'g3'
    G4 = 'g4'
    G5 = 'g5'
    G6 = 'g6'
    G7 = 'g7'
    G8 = 'g8'
    H1 = 'h1'
    H2 = 'h2'
    H3 = 'h3'
    H4 = 'h4'
    H5 = 'h5'
    H6 = 'h6'
    H7 = 'h7'
    H8 = 'h8'

''' board layout  
    white's perspective:
    8
    7
    6
    5
    4
    3
    2
    1
     a b c d e f g h

    black's perspective:
    1
    2
    3
    4
    5
    6
    7
    8
     h g f e d c b a
'''
#by default in white's perspective. flipped if pawn is black.
#the lists should not be mutated, each class should make a copy and store it in __init__
rows = [ '1', '2', '3', '4', '5', '6', '7', '8' ]
cols = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ]

class Pawn:
    def __init__(self, color: Color, current_pos: str):
        self.color = color
        self.current_pos = current_pos
        self.rows = rows[::] if color == Color.white else rows[::-1]
        self.cols = cols[::] if color == Color.white else cols[::-1]

    #takes in a position, and returns and array with the number of steps specified
    #as the board positions
    def move_forward(self, num_steps: int) -> List[str]:
        print(num_steps)

        #get index of the current x coord
        x, y = self.current_pos #ex: extracts a, 1 from 'a1'
        y_index = self.rows.index(y)
        steps: List[str] = []
        #we want n steps forward, so x coord remains the same and y increases by n
        for i in range(y_index + 1, y_index + num_steps + 1):
            print(f'y index: {y_index} new y index: {y_index + num_steps} new y value: {self.rows[y_index+i]} i value {i}')
            steps.append(f'{x}{self.rows[ i ]}')

        return steps
    # returns the possible moves a piece can make
    def show_moves(self) -> List[str]:
        # returns two available moves if pawns are in starting position
        for  char in cols:
            if self.color == Color.white and self.current_pos == f'{char}2':
                return self.move_forward(2)

            if self.color == Color.black and self.current_pos == f'{char}7':
                return self.move_forward(2)

        return self.move_forward(1)
        

    # filteres show_moves() and returns only the valid moves a piece can make
    def show_valid_moves(self):
        pass
        
    


p_white_start = Pawn(Color.white, 'a2')
p_white_moved = Pawn(Color.white, 'a3')


p_black_start = Pawn(Color.black, 'a7')
p_black_moved = Pawn(Color.black, 'a6')

print('white start a2: ', p_white_start.show_moves())
print('white moved a3: ', p_white_moved.show_moves())

print('black start a7: ', p_black_start.show_moves())
print('p_black_moved a6: ', p_black_moved.show_moves())

