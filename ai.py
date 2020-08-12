import numpy
import threading
from board import board
from client import client
from time import sleep

class player(client):

    def __init__(self, base,key, w = None, depth = 0):
        super().__init__(base, key)
        self.key = key
        self.weights = w
        self.depth = depth
        self.wights = w
    
    def eval_func(self, board_obj, player):
        gamma = self.weights['gamma']
        mobility_w = self.weights['mobility']
        amount_w = self.weights['amount']
        board = board_obj
        if board_obj.has_ended() and board_obj.count(player) > 32:
            score = player * 500
        score = 0
        player0_moves = len(board.potential_moves(1))
        player1_moves = len(board.potential_moves(-1))

        if player == 1:
            player0_moves = player0_moves * gamma
        else:
            player1_moves = player1_moves * gamma

        
        diff_moves = player0_moves - player1_moves
        score += diff_moves * mobility_w

        count = board.count(player)
        score += count * amount_w

        

        return score
    
    
    def minimax(self,pos, depth , alpha, beta, maxing_player):

        helper = board(init_board = pos)
        # print(helper.view_board,depth,maxing_player)
        
        if maxing_player:
            player = 1
        else:
            player = -1
        
       
        if depth == 0 or helper.has_ended():
            # print('finished', self.eval_func(helper, player))
            return self.eval_func(helper, player)

        
        if maxing_player:
            # print('max')
            maxEval  = -1000

            children = helper.potential_moves(player)
            for child in children:
                new_pos = helper.pred_move(child[0], child[1], player)
                
                eval = self.minimax(new_pos, depth-1, alpha, beta, False)
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            
            return maxEval
        
        else:
            # print('min')
            min_eval = 1000
            children = helper.potential_moves(player)
            

            for child in children:
                new_pos = helper.pred_move(child[0], child[1], -1)
                eval = self.minimax(new_pos, depth-1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            
            return min_eval

    def test_minimax(self, board_obj):
        pred = board_obj
        move = pred.potential_moves(1)[0]
        pos = pred.pred_move(move[0], move[1], 1)
        score = self.minimax(pos, 2, -1000, 1000, False)
        # print(score)
    
    def pick_best(self, board_obj):
        
        pred = board_obj
        
        moves = pred.potential_moves(1)
        
        best_move = None
        
        best_score = -10000
        # print(moves, self.key)
        if __name__ == '__main__':
            for move in moves:
                # print(move)
                pos = pred.pred_move(move[0], move[1], 1)
                # print(pos)
                score = self.minimax(pos, 2, -1000, 1000, False)
                if score > best_score:
                    best_move = move
                    best_score = score
            
        return best_move

    def make_move(self):
        
        board_obj = board(self.board)
        move = self.pick_best(board_obj)
        x, y = move[0], move[1]
        self.move(x,y)
    
    def play(self):
        while True:
            if self.needed:
                self.make_move()
            sleep(0.1)


url = 'http://127.0.0.1:5000/'
key0 = 'key0'
key1 = 'key1'
key2 = 'key2'
key3 = 'key3'
def play():
    player0_w = {'gamma': 1, 'mobility':0, 'amount': 1}
    player1_w = {'gamma': 1, 'mobility':0, 'amount': 1}
    player2_w = {'gamma': 1, 'mobility':1, 'amount': 0}
    player3_w = {'gamma': 1, 'mobility':1, 'amount': 1}

    player0 = player(url, key0, w=player0_w)
    player1 = player(url, key1, w=player1_w)
    player2 = player(url, key2, w=player2_w)
    player3 = player(url, key3, w=player3_w)

    t0 = threading.Thread(target=player0.play, args=())
    t1 = threading.Thread(target=player1.play, args=())
    t2 = threading.Thread(target=player2.play, args=())
    t3 = threading.Thread(target=player3.play, args=())

    t0.start()
    t1.start()
    t2.start()
    t3.start()


play()

def test():
    player2 = player(url, key2)
    player2.play()

# test()