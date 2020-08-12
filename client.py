import requests
import numpy as np
import time

class client:

    def __init__ (self,base,key):

        self.base_url = base

        self.board_ep =  base + 'boards/' + key
        self.move_needed_ep =  base + 'move_needed/' + key
        self.name_ep =  base + 'set_name/' + key
        self.move_ep =  base + 'move/' + key

    @property
    def board(self):
        r = requests.get(self.board_ep).json()
        data = r['boards']
        data = np.array(data)[0]
        return data

    @property
    def needed(self):
        r = requests.get(self.move_needed_ep).json()
        return r['needed']

    def change_name(self):
        while True:
            r = requests.post(self.name_ep + '/yeet/')
            print(r.json())
            time.sleep(0.1)
            r = requests.post(self.name_ep + '/big/')
            time.sleep(.1)
    
    def move(self, x, y):
        
        r = requests.post(self.move_ep + ('/%i/%i')% (y,x)) 
        print(r.text)
        print(r.url)

# url = 'http://127.0.0.1:5000/'
# key0 = 'key0'
# key1 = 'key1'
# key2 = 'key2'
# key3 = 'key3'
# player0 = client(url, key0)
# player1 = client(url, key1)
# player2 = client(url, key2)
# player3 = client(url, key3)




