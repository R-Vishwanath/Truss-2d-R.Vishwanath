import math
def length_mem(mem,coord):
    l=[]
    for i in range(len(mem)):
        k1=mem[i][0]-1
        k2=mem[i][1]-1
        o=pow(pow(coord[k1][0]-coord[k2][0],2)+pow(coord[k1][1]-coord[k2][1],2),0.5)
        l.append(o)
    return l

