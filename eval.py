
def eval(node_s,s):
    if s=="p":
        vv=1
    else:
        vv=-1
    node_s.value = (vv*3 * node_s.blue_m)+(vv*2 * node_s.red_m)