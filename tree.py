import numpy as np

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


T5 = Tree(None,(5,5),1)
T6 = Tree(None,(5,4),1)

T1 = Tree(T5,(2,2),0)
T1.add_branch(T6)
T2 = Tree(None,(2,3),1)

T3 = Tree(T1,(2,1),0)
T4 = Tree(T2,(2,7),0)

T = Tree(T3,(2,4),0)
T.add_branch(T4)

print(T.to_string())

print(T.get_best_move())

