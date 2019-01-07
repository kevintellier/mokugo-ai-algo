import numpy as np
import random
import sys
import time

PIONS = 3
N = 4
END = 1

#BOARD VALUES
EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = 2

def eval_position(P):
    c1_max = 0
    c2_max = 0
    for j in range(0,N):
        C1=0
        C2=0
        for i in range(0,N):#horizontal
            if P[i][j] == PLAYER_1:
                C2=0
                C1+=1
                if C1 == PIONS : return 1000
            if P[i][j] == PLAYER_2:
                C1=0
                C2+=1
                if C2 == PIONS : return -1000
            if P[i][j] == EMPTY:
                C1=0
                C2=0
            if C1 > c1_max:
                c1_max = C1
            if C2 > c2_max:
                c2_max = C2

    for i in range(0,N):
        C1=0
        C2=0
        for j in range(0,N):#vertical
            if P[i][j] == PLAYER_1:
                C2=0
                C1+=1
                if C1 == PIONS : return 1000
            if P[i][j] == PLAYER_2:
                C1=0
                C2+=1
                if C2 == PIONS : return -1000
            if P[i][j] == EMPTY:
                C1=0
                C2=0
            if C1 > c1_max:
                c1_max = C1
            if C2 > c2_max:
                c2_max = C2

    for rs in range(0,N-PIONS+1):
        C1=0
        C2=0
        i = rs
        j = 0
        while i < N and j < N:
            if P[i][j] == PLAYER_1:
                C2=0
                C1+=1
                if C1 == PIONS : return 1000
            if P[i][j] == PLAYER_2:
                C1=0
                C2+=1
                if C2 == PIONS : return -1000
            if P[i][j] == EMPTY:
                C1=0
                C2=0
            i+=1
            j+=1
            if C1 > c1_max:
                c1_max = C1
            if C2 > c2_max:
                c2_max = C2

    for cs in range(1,N-PIONS+1):
        C1=0
        C2=0
        i = 0
        j = cs
        while i < N and j < N:
            if P[i][j] == PLAYER_1:
                C2=0
                C1+=1
                if C1 == PIONS : return 1000
            if P[i][j] == PLAYER_2:
                C1=0
                C2+=1
                if C2 == PIONS : return -1000
            if P[i][j] == EMPTY:
                C1=0
                C2=0
            if C1 > c1_max:
                c1_max = C1
            if C2 > c2_max:
                c2_max = C2
            i+=1
            j+=1

    for rs in range(0, PIONS):
        C1=0
        C2=0
        i = N-1
        j = rs
        while i >= 0 and j < N:
            print(i,j)
            if P[i][j] == PLAYER_1:
                C2=0
                C1+=1
                if C1 == PIONS : return 1000
            if P[i][j] == PLAYER_2:
                C1=0
                C2+=1
                if C2 == PIONS : return -1000
            if P[i][j] == EMPTY:
                C1=0
                C2=0
            i-=1
            j+=1
            if C1 > c1_max:
                c1_max = C1
            if C2 > c2_max:
                c2_max = C2

    for cs in range(PIONS-1, N-1):
        C1=0
        C2=0
        i = cs
        j = 0
        while i >= 0 and j < N:
            print(i,j)
            if P[i][j] == PLAYER_1:
                C2=0
                C1+=1
                if C1 == PIONS : return 1000
            if P[i][j] == PLAYER_2:
                C1=0
                C2+=1
                if C2 == PIONS : return -1000
            if P[i][j] == EMPTY:
                C1=0
                C2=0
            if C1 > c1_max:
                c1_max = C1
            if C2 > c2_max:
                c2_max = C2
            i-=1
            j+=1

    print(c1_max,c2_max)
    return (c1_max - c2_max) * 100



def create_board():
    print("Board Created")
    P = [[0] * N for _ in range(N)]
    return P;

def play(P, player):
    print("-----Player " + str(player) + "------\n")
    x = int(input("Position x : "))-1
    y = int(input("Position y : "))-1
    if P[y][x] == 0 and x >= 0 and y >= 0 and x <= N and y <= N:
        print("Joueur " + str(player) + " : Pion en " + str(x+1) + ";" + str(y+1) + "\n")
        P[y][x] = player
    else:
        print("Invalid position ! ")
        play(P,player)
    return (x,y)

def print_board(P):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in P]))
    print("\n")
    return 0

def main():
    print("Init")
    end = False
    #INIT
    P = create_board()
    #GAME
    while(end != True):
        print_board(P)
        hint = play(P,PLAYER_1)
        print_board(P)
        e = eval_position(P)
        if(e == 1000):
            print("White wins !")
            break
        elif(e == -1000):
            print("Black wins !")
            break
        """hint = play(P,PLAYER_2)
        print_board(P)
        e = eval_position(P)
        if(e == 1000):
            print("White wins !")
            break
        elif(e == -1000):
            print("Black wins !")
            break"""
    return 0

if __name__ == "__main__":
    main()
