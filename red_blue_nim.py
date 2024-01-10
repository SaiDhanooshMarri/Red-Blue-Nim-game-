
import sys
import math
from piles import piles,g_tree
from child_path import child_node     
from human import human
from computer import computer

x = int(sys.argv[1])
y = int(sys.argv[2])
if len(sys.argv)>=4:
    z=str(sys.argv[3])
    z=z.lower()
    if len(sys.argv)==5:
        zz=int(sys.argv[4])
    else:
        zz=math.inf 
else:
    z="computer"
    zz=math.inf 
   

if z=="human":
    while True: 
        x,y=human(x,y,zz)
        x,y=computer(x,y,zz)

else:
    while True:    
        x,y=computer(x,y,zz)
        x,y=human(x,y,zz)

    







