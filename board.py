import numpy as np
import time



class board:
    

    def __init__(self, init_board =  None):

        if type(init_board) != type(np.array(1)):
            black_pos = [[4,3], [3,4]]
            white_pos = [[3,3], [4,4]]

            zeros = np.zeros((8,8))

            for pos in black_pos:
                zeros[pos[0]][pos[1]] = -1

            for pos in white_pos:
                zeros[pos[0]][pos[1]] = 1

            self.internal_board = zeros
        
        else:
            self.internal_board = init_board

    def get_moveable (self, x, y, player):
        rel_neighbors = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[-1,1], [1,-1]]
        board = self.internal_board
        def check_movable(x,y,v, player, tiles):
            
            if tiles == None:
                return None

            x_cord = x + v[0]
            y_cord = y + v[1]
            
            if x_cord < 0 or x_cord > 7 or y_cord < 0 or y_cord > 7:
                return None

            tile = board[x_cord][y_cord]

            if tile == 0:
                return None
            
            if tile == player and len(tiles) == 0:
                return None
            
            if tile == player:
                return tiles          

            if tile == -player:
                tiles.append([x_cord,y_cord])
                return  check_movable(x_cord,y_cord,v, player,tiles)
        
        moveable = []
        for rel_neighbor in rel_neighbors:
            tiles = []
            tiles = check_movable(x,y,rel_neighbor,player,tiles)
            if not tiles == None:
                for tile in tiles:
                    moveable.append(tile)
        
        moveable.append([x,y])

        return moveable
        
       

    def pred_move(self,x,y,player):
        
        board = np.copy(self.internal_board)
        
        
        moveable = self.get_moveable(x,y,player)
        
        if len(moveable) >1:
            for cord in moveable:
                board[cord[0]][cord[1]] = player
        
        return board
        

    def good_move(self,x,y,player):
        if len(self.get_moveable(x,y,player)) > 1:
            return True
        
        return False
    
    def potential_moves(self, player):
        rel_neighbors = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[-1,1], [1,-1]]
        result = np.where(self.internal_board != 0)
        occupied= list(map(list, zip(result[0], result[1])))

        adjacent_moves = []
        for node in occupied:
            for v in rel_neighbors:
                x = node[0] + v[0]
                y = node[1] + v[1]
                cord = [x,y]
                if x >= 0 and x <= 7 and y >= 0 and y <= 7: 
                    if cord not in occupied and cord not in adjacent_moves:
                        adjacent_moves.append(cord)
        moves = []
        for move in adjacent_moves:
            x = move[0]
            y = move[1]
            if self.good_move(x,y,player):
                moves.append(move)

        return moves
    
    def count(self, player):
        result = np.where(self.internal_board == player)
        count = list(map(list, zip(result[0], result[1])))
        return len(count)
    
    def has_ended(self):
        
        player0_moves = len(self.potential_moves(1))
        player1_moves = len(self.potential_moves(-1))
        
        if player0_moves == 0 or player1_moves == 0:
            return True
        else:
            return False


    @property
    def board(self):
        return self.internal_board

    @property
    def view_board(self):
        return self.internal_board.T
        

# board = board()
# board.move(5,3,1)

# # print(board.board)

# start = time.time()
# board.move(5,2,-1)
# # board.potential_moves(1)
# end = time.time()

# print(end-start)

# # print(board.board)