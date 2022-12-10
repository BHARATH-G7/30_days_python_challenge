#!/usr/bin/python3

import random
player_1=input("rock or paper or scissor :").lower()
player_2=random.choice(['rock','paper','scissor']).lower()
print("player-2 selected: ",player_2)
if player_1=='rock' and player_2=='paper':
    print("player-2 won")
elif player_1=='paper' and player_2=='scissor':
    print("player-2 won")
elif player_1=='scissor' and player_2=='rock':
    print("player-2 won")
elif player_1==player_2:
    print("TIE")
else:
    print("player-1 won")
    
