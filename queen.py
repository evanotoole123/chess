from piece import Piece, Color
from typing import List
from illegalMoveError import IllegalMoveError

class Queen(Piece):
    # Piece is initialized through colour and current position,(__init__ method in Piece class)


    # returns the non validated possible moves a piece can make
    def move(self, new_pos: str) -> List[str]:
        x, y = self.current_pos[0], self.current_pos[1]
        x_index = self.cols.index(x)
        y_index = self.rows.index(y)

        #remove the current position from the possible moves
        possible_x = self.cols.copy()
        possible_x.pop(x_index)
        possible_y = self.rows.copy()
        possible_y.pop(y_index)

        #create our possible_moves array (these are the squares we can move to 
        #if there are no pieces in the way)
        possible_moves = []
        for i in possible_x: possible_moves.append(f'{i}{y}')
        for j in possible_y: possible_moves.append(f'{x}{j}')
        
        if new_pos in possible_moves:
            
            change_in_column = ord(self.current_pos[0]) - ord(new_pos[0])
            change_in_row =  int(self.current_pos[1]) - int(new_pos[1])
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
        
        i = 1
        try:
            for i in range(8):
                a = self.move_diagonally(i)
                i += 1
        except:
            pass

        
        #print(a)
  

        if new_pos in a[0]:
            half = len(a[0])//2 -1
            first = a[0][:half]
            second = a[0][half:]
            if new_pos in first:
                return first
            else:
                return second
        elif new_pos in a[1]:
            half = len(a[1])//2 -1
            first = a[1][:half]
            second = a[1][half:]
            if new_pos in first:
                return first
            else:
                return second
            
        elif new_pos in a[2]:
            half = len(a[2])//2 -1
            first = a[2][:half]
            second = a[2][half:]
            if new_pos in first:
                return first
            else:
                return second
            
        elif new_pos in a[3]:
            half = len(a[3])//2 -1
            first = a[3][:half]
            second = a[3][half:]
            if new_pos in first:
                return first
            else:
                return second

        raise IllegalMoveError("this piece can not move in this way (in Queen.py)")
    
    def take():
        pass
    

print('TESTING QUEEN--------')
queen = Queen('white', 'd4')
print(queen.move('a1'))
print(queen.move('d7'))