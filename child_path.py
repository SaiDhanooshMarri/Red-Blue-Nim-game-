
from eval import eval
def alpha(nodde,node_s):
    if node_s.value>=nodde.beta:
        nodde.chhild.pop(1)
        nodde.alpha=node_s.value 
    elif node_s.value>nodde.alpha:
        nodde.alpha=node_s.value
def beta(nodde,node_s):
    if node_s.value<=nodde.alpha:
        nodde.chhild.pop(1)
        nodde.beta=node_s.value
    elif node_s.value<nodde.beta:
        nodde.beta=node_s.value

def child_node(nodde):
    
    for node_s in nodde.chhild:
        child_node(node_s)
        node_s.alpha,node_s.beta=nodde.alpha,nodde.beta
        if not node_s.chhild:
            if nodde.length%2==0:
                eval(node_s,"n")
                alpha(nodde,node_s)
            else:
                eval(node_s,"p")
                beta(nodde,node_s)
        else:
            if node_s.length%2==0:
                if len(node_s.chhild)>1:
                    node_s.value = max(node_s.chhild[0].value, node_s.chhild[1].value)
                else:
                    node_s.value=node_s.chhild[0].value
                if node_s.value<=nodde.alpha:
                    nodde.beta=node_s.value
                elif node_s.value<nodde.beta:
                    nodde.beta=node_s.value
            else:
                if len(node_s.chhild)>1:
                    node_s.value = min(node_s.chhild[0].value, node_s.chhild[1].value)
                else:
                    node_s.value=node_s.chhild[0].value
                if node_s.value>=nodde.beta:
                    nodde.alpha=node_s.value
                elif node_s.value>nodde.alpha:
                    nodde.alpha=node_s.value