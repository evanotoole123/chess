from piece import Piece, Color
from typing import List
from illegalMoveError import IllegalMoveError

class Bishop(Piece):
    # Piece is initialized through colour and current position,(__init__ method in Piece class)

    def __repr__(self):
        return f'Bishop(colour= {self.color}, position= {self.current_pos})'


    def __str__(self):
        return f'BISHOP:{self.current_pos}'
    
    # returns the non validated possible moves a piece can make
    def move(self, new_pos: str) -> List[str]:
        x, y = self.current_pos[0], self.current_pos[1]
        x_index = self.cols.index(x)
        y_index = self.rows.index(y)

        i = 1
        for i in range(8):
            a = self.move_diagonally(i)
            i += 1
       

        
        #print(a)
        path = []

        if new_pos in a[0]:
            index = a[0].index(new_pos)
            path = a[0][:index+1]
            return path
            
        elif new_pos in a[1]:
            index = a[1].index(new_pos)
            path = a[1][:index+1]
            return path
            
        elif new_pos in a[2]:
            index = a[2].index(new_pos)
            path = a[2][:index+1]
            return path
            
        elif new_pos in a[3]:
            index = a[3].index(new_pos)
            path = a[3][:index+1]
            return path

        raise IllegalMoveError("this piece can not move in this way (in bishop.py)")
    
    def take():
        pass

print('TESTING BISHOP--------')
bishop = Bishop('white', 'c4')
print(bishop.move('b3'))
print(bishop.move('g8'))