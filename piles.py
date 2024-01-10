import math

class piles:
    def __init__(self, red_m, blue_m,length,parent,depth):
        self.red_m = red_m
        self.blue_m = blue_m
        self.chhild = []
        self.value = None
        self.length=length
        self.alpha = -math.inf
        self.beta = math.inf
        self.parent=parent
        self.depth=depth

    def g_child(self):
        if self.depth>0:
            if self.red_m > 0 and self.blue_m > 0:
                if self.red_m > 0:
                    self.chhild.append(piles(self.red_m - 1, self.blue_m,self.length + 1,self,self.depth-1))
                    
                if self.blue_m > 0:
                    self.chhild.append(piles(self.red_m, self.blue_m - 1,self.length + 1,self,self.depth-1))


def g_tree(nodde):
    nodde.g_child()
    for child in nodde.chhild:
        g_tree(child)