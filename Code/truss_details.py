import math
def truss_det():
    j=int(input('number of coordinates :'))
    coord=[]
    for i in range(j):
        print('coordinate '+str(i+1))
        coord.append([float(input(f'x({i+1})=')),float(input(f'y({i+1})='))])
    m=int(input('number of memebers :'))
    mem=[]
    for i in range(m):
        print('member no :'+str(i+1))
        mem.append([int(input('cordinate no :')),int(input('to coordinate no :'))])
    ns = int(input('number of supports :'))
    support_cood_det = []
    rnx=0
    for i in range(ns):
        print('for support no '+str(i+1))
        support_type = input('type "p"-pinned or type "r"-roller :')
        if support_type == 'p':
            reactions = 2
            up=1
            n=1
            rnx=rnx+2
        elif support_type == 'r':
            if input('type "x" for orientation of support along x axis or "y" for orientation of support along y axis :')=='x':
                reactions=1
                up=0
                n=1
                rnx=rnx+1
            else:
                reactions = 1
                up=1
                n=0
                rnx=rnx+1
        support_cood_det.append([coord[int(input('support coordinate no:'))-1], reactions,n,up])#the two 0s will be used for writing reactions
    a=input('are all members having same area  (t/f)')
    area=[]
    if a=='t':
        areaval=float(input('in units of mm2 '))
        for i in range(len(mem)):
            area.append(areaval)
    elif a=='f':
        for i in range(len(mem)):
            print('for member no {} the area of the member is (units of mm2)'.format(i+1))
            area.append(float(input()))
    a=input('are all members having same moduli of elasticity  (t/f) ')
    E=[]
    if a=='t':
        Eval=float(input('in units of Gpa '))
        for i in range(len(mem)):
            E.append(Eval)
    elif a=='f':
        for i in range(len(mem)):
            print('for member no {} the E of the member is (units of Gpa ) '.format(i+1))
            E.append(float(input()))
    return [coord,mem,support_cood_det,rnx,area,area,E]


