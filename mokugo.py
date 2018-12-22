import numpy as np
import random
import sys

sys.setrecursionlimit(1000000)

PIONS = 2
N = 2
END = 1

#BOARD VALUES
EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = 2

class Tree:
    def __init__(self, branch, hint, score):
        self.branch = []
        self.branch.append(branch)
        if branch is not None:
            self.score = score + branch.score
        else:
            self.score = score
        self.hint = hint

    def get_branch(self, number):
        return self.branch[number]
    
    def add_branch(self, tree):
        self.branch.append(tree)
        self.score += tree.score
    
    def get_best_move(self):
        score_tab = [0] * len(self.branch)
        for i in range(len(self.branch)):
            score_tab[i] = self.branch[i].score
        return self.branch[np.argmax(score_tab)].hint
    
    def get_score(self):
        return self.score
    
    def add_score(self, score):
        self.score += score

    def to_string(self, layer=0):
        if self is not None:
            ret = "\t"*layer + "Hint : " + str(self.hint) + " | Score : " + str(self.score) + "\n"
            for i in range(len(self.branch)):
                if self.branch[i] is not None:
                    ret += self.branch[i].to_string(layer+1)
            return ret

def eval_position(P,A):
    for j in range(0,N):
        C1=0
        C2=0
        for i in range(0,N):#horizontal
            if P[i][j] == PLAYER_1:
                    C2=0
                    C1+=1
                    if C1 == A:
                        return 1000
            if P[i][j] == PLAYER_2:
                    C1=0
                    C2+=1
                    if C2 == A: 
                        return -1000
            if P[i][j] == EMPTY:
                    C1=0
                    C2=0
    for i in range(0,N):#vertical
        C1=0
        C2=0
        for j in range(0,N):
            if P[i][j] == PLAYER_1:
                    C2=0
                    C1+=1
                    if C1 == A: return 1000
            if P[i][j] == PLAYER_2:
                    C1=0
                    C2+=1
                    if C2 == A: return -1000
            if P[i][j] == EMPTY:
                    C1=0
                    C2=0
    x0 = 0
    y0 = 0
    i=j=0
    """
    while((i,j) != (4,0)):#diag up
        C1=0
        C2=0
        x0+=1
        y0+=1
        i=x0
        j=y0
        while((i < N) and (j < N)):#1 diag
            print("("+str(i)+";"+str(j)+")")
            if P[i][j] == PLAYER_1:
                C2=0
                C1+=1
                if C1 == A: return 1000
            if P[i][j] == PLAYER_2:
                C1=0
                C2+=1
                if C2 == A: return -1000
            if P[i][j] == EMPTY:
                C1=0
                C2=0
            i+=1
            j+=1
    """
    return 0

def create_board():
    print("Board Created")
    P = [[0] * N for _ in range(N)]
    return P;

#Play a hint
def ai_play(P, player, hint):
    (x,y) = hint
    P[x][y] = player
    return P

def play(P, player):
    print("-----Player " + str(player) + "------\n")
    x = int(input("Position x : "))-1
    y = int(input("Position y : "))-1
    if P[x][y] == 0:
        print("Joueur " + str(player) + " : Pion en " + str(x) + ";" + str(y) + "\n")
        P[x][y] = player
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


def construct_tree(T,P,player):
    #Construct descisional Tree
    if not full(P):
        if player == PLAYER_1:
            for possible_hint in calc_possible_hints(P,PLAYER_1,N):
                #player 1
                P = ai_play(P,PLAYER_1,possible_hint)#Play
                if eval_position(P,PIONS) == 1000 and player == 1:#Player 1 won
                    T.add_branch(Tree(None,possible_hint,1))
                else:#Nobody won
                    T.add_branch(Tree(None,possible_hint,0))
            construct_tree(T,P,PLAYER_2)

        if player == PLAYER_2:
            for possible_hint in calc_possible_hints(P,PLAYER_2,N):
                #player 1
                P = ai_play(P,PLAYER_1,possible_hint)#Play
                if eval_position(P,PIONS) == -1000 and player == 2:#Player 2 won
                    T.add_branch(Tree(None,possible_hint,1))
                else:#Nobody won
                    T.add_branch(Tree(None,possible_hint,0))
            construct_tree(T,P,PLAYER_1)
    return 0

def get_best_hint(T):
    if T == None:
        print("Oh probleme")
        return (0,0)
    return T.branch[np.argmax(T.branch)].hint

def full(P):
    for x in range(N):
        for y in range(N):
            if P[x][y] is not 0:
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
    hint = (random.randint(0,N-1), random.randint(0,N-1))
    ai_play(P,PLAYER_1,hint)
    T = Tree(None, hint, 0)
    Pp = P.copy()
    construct_tree(T,Pp,PLAYER_1)
    print(T.to_string())
    #GAME
    while(end != True):
        ai_play(P,get_best_hint(T))
        print_board(P)
        e = eval_position(P,PIONS)
        if(e == 1000):
            print("White wins !")
            break
        elif(e == -1000):
            print("Black wins !")
            break
        hint = play(P,PLAYER_2)
        T = navigate_tree(hint)
        print_board(P)
        e = eval_position(P,PIONS)
        if(e == 1000):
            print("White wins !")
            break
        elif(e == -1000):
            print("Black wins !")
            break
    return 0;

if __name__ == "__main__":
    main()
