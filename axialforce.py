import lengthmember
import linearsoln
def axial_force(coord,mem,loads_with_support,support_soln):
    c=[]
    le=lengthmember.length_mem(mem,coord)
    for i in range(len(coord)):
        a=[]
        b=[]
        for l in range(len(mem)):
            if mem[l][0]==i+1:
                k1=mem[l][1]
                a.append((coord[k1-1][0]-coord[i][0])/le[l])
                b.append((coord[k1-1][1]-coord[i][1])/le[l])
            elif mem[l][1]==i+1:
                k1=mem[l][0]
                a.append((coord[k1-1][0]-coord[i][0])/le[l])
                b.append((coord[k1-1][1]-coord[i][1])/le[l])
            else:
                a.append(0)
                b.append(0)

        c.append(b)
        c.append(a)


    for j in range(2*len(coord)):
        b = len(c[j])
        for i in range(b,2*len(coord)):
            if 2*len(coord)-1-i!=j:
                c[j].append(0)
            else:
                c[j].append(1)

    #summing forces in quadrant
    sumfmatrix=[]
    for i in range(len(coord)):
        sumfX=0
        sumfY=0
        for f in range(len(loads_with_support)):
            if coord[i]==loads_with_support[f][0]:
                sumfX=sumfX+loads_with_support[f][1][0]
                sumfY=sumfY+loads_with_support[f][1][1]
        sumfmatrix.append(-sumfY)
        sumfmatrix.append(-sumfX)

    axial_force_soln = linearsoln.linear_solve(c,sumfmatrix)
    n=[]
    for i in range(len(mem)):
        n.append(axial_force_soln[i])
        print('the axial force in member ' + str(float(i + 1)) + '= ' + str(round(n[i], 2)))
    return n

def axial_force_wop(coord,mem,loads_with_support,support_soln):
    c=[]
    le=lengthmember.length_mem(mem,coord)
    for i in range(len(coord)):
        a=[]
        b=[]
        for l in range(len(mem)):
            if mem[l][0]==i+1:
                k1=mem[l][1]
                a.append((coord[k1-1][0]-coord[i][0])/le[l])
                b.append((coord[k1-1][1]-coord[i][1])/le[l])
            elif mem[l][1]==i+1:
                k1=mem[l][0]
                a.append((coord[k1-1][0]-coord[i][0])/le[l])
                b.append((coord[k1-1][1]-coord[i][1])/le[l])
            else:
                a.append(0)
                b.append(0)

        c.append(b)
        c.append(a)


    for j in range(2*len(coord)):
        b = len(c[j])
        for i in range(b,2*len(coord)):
            if 2*len(coord)-1-i!=j:
                c[j].append(0)
            else:
                c[j].append(1)

    #summing forces in quadrant
    sumfmatrix=[]
    for i in range(len(coord)):
        sumfX=0
        sumfY=0
        for f in range(len(loads_with_support)):
            if coord[i]==loads_with_support[f][0]:
                sumfX=sumfX+loads_with_support[f][1][0]
                sumfY=sumfY+loads_with_support[f][1][1]
        sumfmatrix.append(-sumfY)
        sumfmatrix.append(-sumfX)

    axial_force_soln = linearsoln.linear_solve(c,sumfmatrix)
    n=[]
    for i in range(len(mem)):
        n.append(axial_force_soln[i])
    return n
