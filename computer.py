
import sys
from piles import piles,g_tree
from child_path import child_node     
def action_required(nodde):
    cc="R" if nodde.chhild[0].value>=nodde.chhild[1].value else "B"
    return cc
def computer(x,y,zz):
    if x==0:
        score=y*3
        print('With a score of :',score," Computer wins")
        sys.exit()
    elif y==0:
        score=x*2
        print('With a score of :',score," Computer wins")
        sys.exit()
    else:
        print("Computers takes turn")
        print(x," Red ",y," Blue piles are remaining ")
        start_tree = piles(x, y,0,None,zz)
        g_tree(start_tree)
        child_node(start_tree)
        act=action_required(start_tree)
        if act=="R":
            x-=1
        else:
            y-=1
        print("Computers choices is ",act)
        return x,y
    