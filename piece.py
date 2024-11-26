from abc import ABC, abstractmethod
from enum import Enum
from typing import List

class Color(Enum):
    white = 'white'
    black = 'black'

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

class Piece(ABC):
    def __init__(self, color: Color, current_pos: str):
        self.color = color
        self.current_pos = current_pos
        self.rows = rows if color == Color.white else rows[::-1]
        self.cols = cols if color == Color.white else cols[::-1]

     #takes in a number of steps and returns and array with the cells of the board corresponding 
    #to the steps with respect to the current position
    def move_forward(self, num_steps: int) -> List[str]:
        print(num_steps)

        x, y = self.current_pos #ex: extracts a, 1 from string 'a1'
        y_index = self.rows.index(y)
        steps: List[str] = []

        for i in range(y_index + 1, y_index + num_steps + 1):
            steps.append(f'{x}{self.rows[ i ]}')

        return steps

    @abstractmethod
    def show_valid_moves(self) -> List[str]:
        pass

    @abstractmethod
    def show_take_moves(self) -> List[str]:
        pass
