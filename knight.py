from piece import Piece, Color
from typing import List
from illegalMoveError import IllegalMoveError

class Knight(Piece):
    # Piece is initialized through colour and current position,(__init__ method in Piece class)


    # returns the non validated possible moves a piece can make
    def move(self, new_pos: str) -> List[str]:
      

        x, y = self.current_pos[0], self.current_pos[1]
        x_index = self.cols.index(x)
        y_index = self.rows.index(y)


        possible_moves = []
        possible_squares = []
        for i in range(len(self.cols)):
            for j in range(len(self.rows)):
                possible_squares.append(f'{self.cols[i]}{self.rows[j]}')

        #print(possible_squares)

        #the following adds all moves which we can move 3 one direction and then 1 left or right.
        possible_moves = self.calculate_possible(possible_squares, x, y)
        path = []

        if new_pos in possible_moves:
            path.append(new_pos)
            return path
                       
        raise IllegalMoveError('new_pos is not a legal move for this piece (error in knight.py)')
    
    def take():
        pass

    def calculate_possible(self, possible_squares, x, y):
        possible_moves = []
        for square in possible_squares:
            if ((((chr(ord(square[0]) - 2) == x) or chr(ord(square[0]) + 2) == x))\
                and (((int(square[1]) - 1) == int(y)) or (int(square[1]) + 1 == int(y)))):

                possible_moves.append(square)
            
            elif (((int(square[1]) - 2 == int(y))) or (int(square[1]) + 2 == int(y)))\
                 and ((chr(ord(square[0]) - 1) == x) or (chr(ord(square[0]) + 1) == x)):
                
                possible_moves.append(square)
        return possible_moves



print('TESTING KNIGHT-----------')
knight = Knight('white', 'd4')
print(knight.move('b5'))