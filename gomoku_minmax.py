from copy import deepcopy

N = 4
PIONS = 3
PLAYER_1 = 1
PLAYER_2 = 2
EMPTY = 0

class Node:
    def __init__(self, child, hint, score):
        self.childs = []
        self.childs.append(child)
        self.score = score
        self.hint = hint

    def add_child(self, child):
        self.childs.append(self)

    def is_terminal_node(self):
        if self.childs is None:
            return True
        else:
            return False

    def to_string(self):
        if self is is_terminal_node():
            return self.hint[0] + ";" + self.hint[1] + " : " + self.score + "\n"
        else:
            string += to_string(self)

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

def possible_hints(P):
	hints = []
	for x in range(N):
		for y in range(N):
			if P[x][y] == 0:
				hints.append((x,y))
	return hints

def MinMax(node, depth, player, P):
	if depth == 0 or node is not None or node.is_terminal_node():
            return node.score
	if player is PLAYER_1:
	    value = float("-inf")
            for child in node.childs:
                value = max(value,MinMax(child, depth-1, PLAYER_2, P))
	else:
            value = float("inf")
	    for child in node.childs:
	        value = min(value, MinMax(child, depth-1, PLAYER_1, P))

def construct_nodes(node,P,player,depth):
    if depth == 0:
    	return
    else:
	for hint in possible_hints(P):
            Pp = deepcopy(P)
	    Pp[hint[0]][hint[1]] = player#Place pion
	    score = eval_position(P)
	    child = Node(None, hint, score)
	    node.add_child(child)
        if player is PLAYER_1:
	    construct_nodes(child,Pp,2,depth-1)
        else:
	    construct_nodes(child,Pp,1,depth-1)

def main():
    P = [[0]*N for _ in range(N)] 
    node = Node(None,(0,0),0)
    print("---Nodes Started---\n")
    construct_nodes(node,P,2,4)
    print("---Nodes OK---\n");
    hint = MinMax(node,3,1,P)
    print(hint)
main()
    
