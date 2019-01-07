"""
Minmax algorithm applied to gomoku game
@Kevin TELLIER
"""

import numpy as np
from copy import deepcopy
import random
import sys
import time

sys.setrecursionlimit(1000000)

DEPTH = 4
WIN_WEIGHT = 10000
PIONS = 3
N = 4
END = 1

#BOARD VALUES
EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = 2

class Tree:
    def __init__(self, depth, branch, hint, score):
        self.depth = depth
        self.father = None
        self.branch = []
        self.branch.append(branch)
        if branch is not None:
            self.score = score + branch.score
        else:
            self.score = score
        self.hint = hint

    def report_score(self):
        if self.father != None:
            self.father.score += self.score
            self.father.report_score()
        else: return 0

    def get_next_branch(self, pos):
        for branch in self.branch:
            if branch != None:
                if pos == branch.hint:
                    return branch
        return None

    def add_branch(self, tree):
        tree.father = self
        self.branch.append(tree)
        self.score += tree.score
        self.report_score()
    
    def get_best_branch(self):
        best_branch = None
        score_max = -99999999999999999
        for branch in self.branch:
            if branch != None:
                if branch.score > score_max:
                    best_branch = branch
                    score_max = branch.score
        return best_branch

    def to_string(self, layer=0):
        if self is not None:
            ret = "\t"*layer + "Hint : " + str(self.hint[0]+1) + ";" + str(self.hint[1]+1) + " | Score : " + str(self.score) + "\n"
            for i in range(len(self.branch)):
                if self.branch[i] is not None:
                    ret += self.branch[i].to_string(layer+1)
            return ret

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
                if C1 == PIONS : return -WIN_WEIGHT
            if P[i][j] == PLAYER_2:
                C1=0
                C2+=1
                if C2 == PIONS : return WIN_WEIGHT
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
                if C1 == PIONS : return -WIN_WEIGHT
            if P[i][j] == PLAYER_2:
                C1=0
                C2+=1
                if C2 == PIONS : return WIN_WEIGHT
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
                if C1 == PIONS : return -WIN_WEIGHT
            if P[i][j] == PLAYER_2:
                C1=0
                C2+=1
                if C2 == PIONS : return WIN_WEIGHT
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
                if C1 == PIONS : return -WIN_WEIGHT
            if P[i][j] == PLAYER_2:
                C1=0
                C2+=1
                if C2 == PIONS : return WIN_WEIGHT
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
            if P[i][j] == PLAYER_1:
                C2=0
                C1+=1
                if C1 == PIONS : return -WIN_WEIGHT
            if P[i][j] == PLAYER_2:
                C1=0
                C2+=1
                if C2 == PIONS : return WIN_WEIGHT
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
            if P[i][j] == PLAYER_1:
                C2=0
                C1+=1
                if C1 == PIONS : return -WIN_WEIGHT
            if P[i][j] == PLAYER_2:
                C1=0
                C2+=1
                if C2 == PIONS : return WIN_WEIGHT
            if P[i][j] == EMPTY:
                C1=0
                C2=0
            if C1 > c1_max:
                c1_max = C1
            if C2 > c2_max:
                c2_max = C2
            i-=1
            j+=1
    return (c2_max - c1_max) * 100

def create_board():
    print("Board Created")
    P = [[0] * N for _ in range(N)]
    return P;

#Play a hint
def ai_play(P, player, hint):
    (x,y) = hint
    P[x][y] = player
    return P

def del_hint(P,hint):
    (x,y) = hint
    P[x][y] = -1
    return P

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

def calc_possible_hints(P,player,N):
    possible_hints = []
    for x in range(N):
        for y in range(N):
            if P[x][y] == 0:
                possible_hints.append((x,y))
    return possible_hints

#Construct descisional Tree
def construct_tree(T,board,player):
    if T.depth >= 0:
        if full(board) is False:#If board not full
            if player == PLAYER_1:
                for hint in calc_possible_hints(board,player,N):
                    #player 1
                    Pp = deepcopy(board)
                    Pp = ai_play(Pp, PLAYER_1, hint)#Play
                    score = eval_position(Pp)
                    branch = Tree(T.depth-1, None, hint, score)
                    T.add_branch(branch)
                    if score != WIN_WEIGHT:#Didn't win
                        construct_tree(branch,Pp,PLAYER_2)
                    else:
                        return 0

            if player == PLAYER_2:
                for hint in calc_possible_hints(board, player, N):
                    #player 2
                    Pp = deepcopy(board)
                    Pp = ai_play(Pp, PLAYER_2, hint)#Play
                    score = eval_position(Pp)
                    branch = Tree(T.depth-1, None, hint, score)
                    T.add_branch(branch)
                    if score != -WIN_WEIGHT:#Don't lose
                        construct_tree(branch,Pp,PLAYER_1)
                    else:
                        return 0
    return 0

def get_best_hint(T):
    max = 0
    for i in range(len(T.branch)):
        if T.branch[i] != None and T.branch[i].score > max:
            max = i
    return T.branch[max].hint

def full(P):
    for x in range(N):
        for y in range(N):
            if P[x][y] == 0:
                return False
    return True

def navigate_tree(T,hint):
    for branch in T.branch:
        if branch.score == hint:
            return branch

def main():
    print("Init")
    end = False
    #INIT
    P = create_board()
    print_board(P)
    hint = play(P,PLAYER_1)
    print_board(P)
    best_branch = Tree(DEPTH, None, hint, 0)
    Pp = deepcopy(P)
    a = time.clock()
    construct_tree(best_branch, Pp, PLAYER_2)
    b = time.clock()
    print("Temps : " + str(b-a))
    #GAME
    while(end != True):
        best_branch = best_branch.get_best_branch()
        print("Joueur 2 : Pion en " + str(best_branch.hint[0]+1) + ";" + str(best_branch.hint[1]+1) + "\n")
        ai_play(P, PLAYER_2, best_branch.hint)
        print_board(P)
        e = eval_position(P)
        print(e)
        if(e == -WIN_WEIGHT):
            print("1 wins !")
            break
        elif(e == WIN_WEIGHT):
            print("2 wins !")
            break
        hint = play(P,PLAYER_1)
        print_board(P)
        e = eval_position(P)
        print(e)
        if(e == -WIN_WEIGHT):
            print("1 wins !")
            break
        elif(e == WIN_WEIGHT):
            print("2 wins !")
            break
        Pp = deepcopy(P)
        best_branch = Tree(DEPTH, None, hint, 0)
        construct_tree(best_branch, Pp, PLAYER_2)
    return 0;

if __name__ == "__main__":
    main()
