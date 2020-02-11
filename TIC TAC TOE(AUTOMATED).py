#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import random 
from time import sleep
def board():
    return(np.array([[0,0,0],
                     [0,0,0],
                     [0,0,0]]))
def check_place(bd):
    n=[]
    for i in range(len(bd)):
        for j in range(len(bd)):
            if bd[i][j] ==0:
                n.append((i,j))
    return(n)

def allot_place(bd,player):
    select = check_place(bd)
    current_place=random.choice(select)
    bd[current_place]=player
    return(bd)

def winner_row(bd,player):
    for i in range(len(bd)):
        win = True
        
        for j in range(len(bd)):
            if bd[i,j]!=player:
                win=False
                continue
                
        if win == True:
            return(win)
        return(win)

def winner_col(bd,player):
    for i in range(len(bd)):
        win =True
        
        for j in range(len(bd)):
            if bd[i][j]!=player:
                win=False
                continue
                
        if win ==  True:
            return(win)
    return(win)

def winner_diag(bd,player):
    win=True
    for i in range(len(bd)):
        if bd[i,i]!=player:
            win =False
    return(win)

def result(bd):
    winner = 0
    
    for player in [1,2]:
        if(winner_row(bd,player) or winner_col(bd,player) or winner_diag(bd,player)):
            winner=player
        if np.all(bd!=0) and winner ==0:
            winner = -1
        return winner
    
#main function
def tic_tac_toe_game():
    bd,winner,counter = board(),0,1
    print(bd)
    sleep(2)
    
    while winner == 0:
        for player in [1,2]:
            bd=allot_place(bd,player)
            print("The game board after "+str(counter)+" move")
            print(bd)
            sleep(2)
            counter+=1
            winner = result(bd)
            if winner!=0:
                break
    return(winner)

print("THE WINNER IS : " + str(tic_tac_toe_game()))


# In[ ]:




