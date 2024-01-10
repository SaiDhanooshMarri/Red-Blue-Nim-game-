
import sys
from piles import piles,g_tree
from child_path import child_node     
def human(x,y,zz):
    if y==0:
        score=x*3
        print('With a score of :',score, 'human wins')
        sys.exit()
    elif x==0:
        score=y*2
        print('With a score of :',score, 'human wins')
        sys.exit()
    else:
        print(x," Red ",y," Blue piles are remaining ")
        human_choice=input("Enter the Marble which you want to pick (R) or (B)")
        if human_choice=="B":
            y-=1
        else:
            x-=1
        return x,y
        