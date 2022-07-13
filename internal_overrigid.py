import just_rigid
import linearsoln
def statically_indeterminate(mem,coord,support,load,l,E,A):
    ns=len(mem)+3-2*len(coord)
    mem_new=[]
    for i in range(len(mem)-ns):
        mem_new.append(mem[i])
    D_pri,n_pri=just_rigid.just_rigid_(mem_new,coord,support,3,load,l,E,A)

    q=[]
    n_mat=[]
    D_needed=[]
    for i in range(ns):
        q.append(mem[len(mem)-ns+i])
        x1=coord[q[i][0]-1][0]
        y1 = coord[q[i][0] - 1][1]
        x2 = coord[q[i][1] - 1][0]
        y2 = coord[q[i][1] - 1][1]
        li=pow((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2),0.5)
        load_new=[[[x1,y1],[(x1-x2)/li,(y1-y2)/li]],[[x2,y2],[(x2-x1)/li,(y2-y1)/li]]]
        D_i,n_i=just_rigid.just_rigid_(mem_new,coord,support,3,load,l,E,A)
        n_mat.append(n_i)
        x1=D_pri[q[i][0]-1][0]
        y1 = D_pri[q[i][0] - 1][1]
        x2 = D_pri[q[i][1] - 1][0]
        y2 = D_pri[q[i][1] - 1][1]
        D_needed.append(pow((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2),0.5))
        E=2*pow(10,5)
        A=5*pow(10,-3)
    f=[]
    for i in range(len(n_mat)):
        f.append([])
        for j in range(len(n_mat)):
            sum=0
            for k in range(len(mem_new)):
                sum=sum+n_mat[i][k]*n_mat[j][k]*l[k]/(E*A)
            f[i].append(sum)
    ohk=0
    olk=0
    for i in range(len(f)):
        for j in range(len(f[i])):
            if f[i]!=0:
                ohk=1
    for i in range(len(D_needed)):
        if D_needed[i]!=0:
            olk=1
    if olk and ohk!=1:
        X=linearsoln.linear_solve(f,D_needed)
    else:
        X=[]
        for i in range(len(D_needed)):
            X.append(0)
    for i in range(len(X)):
        n_pri.append(X[i])
    for i in range(len(n_pri)):
        print('the axial force in member ' + str(float(i + 1)) + '= ' + str(round(n_pri[i], 2)))
    return n_pri

def statically_indeterminate_wop(mem,coord,support,load,l,E,A):
    ns=len(mem)+3-2*len(coord)
    mem_new=[]
    for i in range(len(mem)-ns):
        mem_new.append(mem[i])
    D_pri,n_pri=just_rigid.just_rigid_(mem_new,coord,support,3,load,l,E,A)
    q=[]
    n_mat=[]
    D_needed=[]
    for i in range(ns):
        q.append(mem[len(mem)-ns+i])
        x1=coord[q[i][0]-1][0]
        y1 = coord[q[i][0] - 1][1]
        x2 = coord[q[i][1] - 1][0]
        y2 = coord[q[i][1] - 1][1]
        li=pow((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2),0.5)
        load_new=[[[x1,y1],[(x1-x2)/li,(y1-y2)/li]],[[x2,y2],[(x2-x1)/li,(y2-y1)/li]]]
        D_i,n_i=just_rigid.just_rigid_(mem_new,coord,support,3,load,l,E,A)
        n_mat.append(n_i)
        x1=D_pri[q[i][0]-1][0]
        y1 = D_pri[q[i][0] - 1][1]
        x2 = D_pri[q[i][1] - 1][0]
        y2 = D_pri[q[i][1] - 1][1]
        D_needed.append(pow((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2),0.5))
        E=2*pow(10,5)
        A=5*pow(10,-3)
    f=[]
    for i in range(len(n_mat)):
        f.append([])
        for j in range(len(n_mat)):
            sum=0
            for k in range(len(mem_new)):
                sum=sum+n_mat[i][k]*n_mat[j][k]*l[k]/(E*A)
            f[i].append(sum)
    ohk=0
    olk=0
    for i in range(len(f)):
        for j in range(len(f[i])):
            if f[i]!=0:
                ohk=1
    for i in range(len(D_needed)):
        if D_needed[i]!=0:
            olk=1
    if olk and ohk!=1:
        X=linearsoln.linear_solve(f,D_needed)
    else:
        X=[]
        for i in range(len(D_needed)):
            X.append(0)
    for i in range(len(X)):
        n_pri.append(X[i])
    return n_pri
