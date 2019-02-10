from copy import deepcopy

N = 4
PIONS = 3
PLAYER_1 = 1
PLAYER_2 = 2
EMPTY = 0
DEPTH = 2
WIN_WEIGHT = 1000

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

	def to_string(self,layer=0):
		if self is not None:
			ret = "\t"*layer + "Hint : " + str(self.hint[0]+1) + ";" + str(self.hint[1]+1) + " | Score : " + str(self.score) + "\n"
			for i in range(len(self.childs)):
				if self.childs[i] is not None:
					ret += self.childs[i].to_string(layer+1)
			return ret

	def printnodes(self,G,depth):
		print(self)
		if len(self.childs) is 0 or depth is 0:
			return
		else:
			for child in self.childs:
				if child is not None:
					G.add_node(child)
					G.add_edge(self, child)
					child.printnodes(G,depth-1)

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
	return (c2_max - c1_max) * 10

def possible_hints(P):
	hints = []
	for x in range(N):
		for y in range(N):
			if P[x][y] == 0:
				hints.append((x,y))
	return hints

def play_ai(P):
	maxi = float('-inf')
	for hint in possible_hints(P):
		P[hint[0]][hint[1]] = PLAYER_2
		tmp = MinMax(DEPTH,PLAYER_2,P)
		print(str(hint) + ":" + str(tmp))
		if tmp > maxi:
			maxi = tmp
			best_hint = hint
		P[hint[0]][hint[1]] = 0
	P[best_hint[0]][best_hint[1]] = PLAYER_2
	print("IA played : " + str(best_hint[0]) + ";" + str(best_hint[1]))

def MinMax(depth, player, P):
	if depth == 0:
		return eval_position(P)

	for hint in possible_hints(P):
		if player is PLAYER_2:
			value = float("-inf")
			P[hint[0]][hint[1]] = PLAYER_2
			value = max(value,MinMax(depth-1, PLAYER_2, P))
			P[hint[0]][hint[1]] = 0
			return value
		else:
			value = float("inf")
			P[hint[0]][hint[1]] = PLAYER_1
			value = min(value,MinMax(depth-1, PLAYER_1, P))
			P[hint[0]][hint[1]] = 0
			return value

def construct_nodes(node,P,player,depth):
	if depth is 0:
		return
	else:
		for hint in possible_hints(P):
			Pp = deepcopy(P)
			Pp[hint[0]][hint[1]] = player#Place pion
			score = eval_position(Pp)
			child = Node(None, hint, score)
			node.add_child(child)
			if player is PLAYER_1:
				construct_nodes(child,Pp,PLAYER_2,depth-1)
			else:
				construct_nodes(child,Pp,PLAYER_1,depth-1)

def print_board(P):
	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in P]))

def play_player(P):
	print("It's your turn you fool")
	hint_x = int(input("x: "))
	hint_y = int(input("y: "))
	while P[hint_y][hint_x] != 0:
		print("Impossible")
		hint_x = int(input("x: "))
		hint_y = int(input("y: "))
	P[hint_y][hint_x] = PLAYER_1
	print("You played : " + str(hint_x) + ";" + str(hint_y))

def main():
	P = [[0]*N for _ in range(N)]
	while 1:
		print_board(P)
		print(eval_position(P))
		play_player(P)
		print_board(P)
		print(eval_position(P))
		if eval_position(P) == -WIN_WEIGHT:
			print("Player 1 won !")
			break
		play_ai(P)
		if eval_position(P) == WIN_WEIGHT:
			print_board(P)
			print("Player 2 won !")
			break
main()
	
