import sys
from ai import player

url = sys.argv[0]
key = sys.argv[1]

ai = player(url,key)
ai.play()