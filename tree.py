import numpy as np
PIONS = 2

class Tree:
    def __init__(self, branch, hint, score):
        self.branch = []
        self.branch.append(branch)
        if branch is not None:
            self.score = score + branch.score
        else:
            self.score = score
        self.hint = hint

    def get_next_branch(self, pos):
        for branch in self.branch:
            if branch != None:
                if pos == branch.hint:
                    return branch
        return -1

    def add_branch(self, tree):
        self.branch.append(tree)
        self.score += tree.score
    
    def get_best_branch(self):
        score_max = -600*PIONS
        for branch in self.branch:
            if branch != None:
                if branch.score > score_max:
                    best_branch = branch
                    score_max = branch.score
        return best_branch

    def to_string(self, layer=0):
        if self is not None:
            ret = "\t"*layer + "Hint : " + str(self.hint) + " | Score : " + str(self.score) + "\n"
            for i in range(len(self.branch)):
                if self.branch[i] is not None:
                    ret += self.branch[i].to_string(layer+1)
            return ret


T0 = Tree(None,(5,5),0)

T1 = Tree(None,(5,4),-100)
T2 = Tree(None,(5,3),-100)
T3 = Tree(None,(5,2),-100)
T4 = Tree(None,(5,1),0)

T5 = Tree(None,(4,5),100)

T6 = Tree(None,(4,4),100)

T7 = Tree(None,(4,3),1000)

T6.add_branch(T7)

T4.add_branch(T6)
T4.add_branch(T5)

T0.add_branch(T1)
T0.add_branch(T2)
T0.add_branch(T3)
T0.add_branch(T4)

print(T0.to_string())
best_branch = T0
print("P1 : " + str(best_branch.hint))

#P2 played 5,5
print("P1 : (5, 5)")

best_branch = T0.get_best_branch()
print("P2 : " + str(best_branch.hint))
#P1 played 5,1

best_branch = best_branch.get_next_branch((4,4))
print("P1 : " + str(best_branch.hint))
#P2 played 4,4

best_branch = best_branch.get_best_branch()
print("P2 : " + str(best_branch.hint))
#P1 played 4,3

