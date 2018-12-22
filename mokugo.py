import numpy as np

PIONS = 3
N = 5
END = 1
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

def create_plate():
    print("Plate Created")
    P = [[0] * N for _ in range(N)]
    return P;

def ai_play(P, player,x,y):
    if P[x][y] == 0:
        P[x][y] = player
        return 0
    else:
        return -1

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
    return 0

def print_plate(P):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in P]))
    print("\n")
    return 0

def calculate_next(T,P,player):
    for i in range(N):
        for j in range(N):
            while(ai_play(P,player,i,j) == -1 and not full(P))#Try to play
            if eval_position(P,PIONS) == 1000 and player == 1:#Player 1 won
                T.add_branch(Tree(NULL,(i,j),1)
            elif evla_position(P,PION) == -1000 and player == 2:#Player 2 won
                T.add_branch(Tree(NULL,(i,j),-1)
            else:#Nobody won
                calculate_next(T,P,player)
            else:

    calculate_next(T

                
    return (x,y);

def full(P):
    for i in range(N):
        for j in range(N):
            if P[x][y] != 0
                return False

def main():
    print("Init")
    end = False
    #INIT
    P = create_plate()
    #GAME
    while(end != True):
        play(P,PLAYER_1)
        print_plate(P)
        e = eval_position(P,PIONS)
        if(e == 1000):
            print("White wins !")
            break
        elif(e == -1000):
            print("Black wins !")
            break
        play(P,PLAYER_2)
        print_plate(P)
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
