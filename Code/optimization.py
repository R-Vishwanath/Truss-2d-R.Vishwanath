import random


def initial_soln(wd,L,h):
    n=random.Random(5,10)
    coord=[]
    coord.append([0,0])
    for i in range(1,n-1):
        coord.append([random.random(i*L/n,(i+1)*L/n),0])
    coord.append([L,0])
    for i in range(n):
        coord.append([random.random(i*L/n,(i+1)*L/n),random.random(0,h)])

    Select_n_mem=[3,4,2,3,4,3,4]
    m=2*(n+n)+3
    mem=[]
    for i in range(n):
        mem.append([i+1,i+2])
    for i in range(n,m):
        for j in range(i,m):
            if coord[i][2]>0 and coord[j][2]>0:
                mem.append([i,j])

    mem.append([0,n])
    mem.append([n-1,2*n-1])
    p=m-len(mem)
    for i in range(p):
        print('incomplete')



