from piece import Piece, Color
from typing import List
from illegalMoveError import IllegalMoveError

class Rook(Piece):
    # Piece is initialized through colour and current position,(__init__ method in Piece class)


    # returns the non validated possible moves a piece can make
    def move(self, new_pos: str) -> List[str]:
        x, y = self.current_pos[0], self.current_pos[1]
        x_index = self.cols.index(x)
        y_index = self.rows.index(y)

        possible_x = self.cols.copy()
        possible_x.pop(x_index)
        possible_y = self.rows.copy()
        possible_y.pop(y_index)

        possible_moves = []
        for i in possible_x: possible_moves.append(f'{i}{y}')
        for j in possible_y: possible_moves.append(f'{x}{j}')

        #
        # triple nested if statements lol
        #print(possible_moves)
       # print(new_pos)

        if new_pos in possible_moves:
            
            change_in_column = ord(self.current_pos[0]) - ord(new_pos[0])
            change_in_row =  int(self.current_pos[1]) - int(new_pos[1])
            #TODO get referee to validate the move
            if change_in_column != 0:
                if ((change_in_column > 0) and self.color == 'white')or\
                    ((change_in_column < 0) and self.color == 'black'):
                    return self.move_right(abs(change_in_column))
                else:
                    return self.move_left(abs(change_in_column))
        
                
            elif change_in_row != 0:
                
                if ((change_in_row > 0) and self.color == 'white')or\
                    ((change_in_row < 0) and self.color == 'black'):
                    
                    return self.move_backward(abs(change_in_row))
                else:
                    return self.move_backward(abs(change_in_row))
               
               
            else:
                raise IllegalMoveError("position has not changed (invalid new_pos value in rook.py)")
            
            
        raise IllegalMoveError('invalid move; piece cannot move in this way (invalid new_pos value in rook.py)')

        
    
    def take(self):
        return

rook = Rook('white', 'a1')
#print('START ROOK TESTING--------')
print(rook.move('a5'))