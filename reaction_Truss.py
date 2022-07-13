import truss_details as td
import truss_drawing
import load_details
import linearsoln
import axialforce
def reaction_in_truss(coord,mem,support,loads):

    Reactions=[]
    #to find b
    d=[]
    q=[]
    for i in range(len(support)):
        x=support[i][0][0]
        y=support[i][0][1]
        b=0
        q.append([])
        o=[x,y]
        for j in range(len(loads)):
            b=b-(loads[j][0][0]-x)*loads[j][1][1]+(loads[j][0][1]-y)*loads[j][1][0]
        d.append(b)
        for p in range(len(support)):
            for k in range(2):
                if support[p][3-k]!=0:
                    q[i].append(support[p][0][k]-o[k])

    t=i+1
    #Ny and Nx not in order (y 1st and then x)

    c1=0
    q.append([])
    for i in range(len(support)):
        for k in range(support[i][1]):

            if k%2==0 and support[i][3]==1:
                q[t].append(0)
                c1=1
            elif k%2!=0 and support[i][2]==1:
                q[t].append(1)
    if c1==1:
        sum1=0
        for i in range(len(loads)):
            sum1=sum1+loads[i][1][0]
        d.append(-sum1)
    else:
        q.pop(t)
        t=t-1


    t=t+1
    q.append([])
    c2=0
    for i in range(len(support)):
        for k in range(2):

            if k%2!=0 and support[i][2]==1:
                q[t].append(0)

            elif k%2==0 and support[i][3]==1:
                q[t].append(1)
                c2 = 1

    sum1=0
    if c2==1:
        for i in range(len(loads)):
            sum1=sum1+loads[i][1][1]
        d.append(-sum1)
    else:
        q.pop(t)
        t=t-1
    #qx=b
    o=len(d)-len(q[0])
    y=len(q[0])
    for i in range(len(q)):
        if i!=y:
            q[i].append(0)
        else:
            q[i].append(1)

    support_soln=linearsoln.linear_solve(q,d)
    load_with_supports=loads

    t=0
    for i in range(len(support)):
        print('support no '+str(i+1))
        o=[]
        for k in range(support[i][1]):
            if k==0 and support[i][3]==1 and support[i][2]==0:
                print('value of Ny= ',end='')
                o.append(support_soln[k+t+i])
                o.append(0)
            elif k==0 and support[i][3]==1 and support[i][2]==1:
                print('value of Ny= ', end='')
                o.append(support_soln[k + t + i])
                o.append(support_soln[k+1+t+i])
            elif k==0 and support[i][3]==0:
                print('value of Nx= ',end='')
                o.append(0)
                o.append(support_soln[k + t + i])
            elif k==1:
                print('value of Nx= ',end='')
            print(support_soln[i + k + t])
        o.reverse()
        load_with_supports.append([support[i][0],o])
        t=t+k
    return(load_with_supports,support_soln)


def reaction_in_truss_wop(coord,mem,support,loads):
    Reactions=[]
    #to find b
    d=[]
    q=[]
    for i in range(len(support)):
        x=support[i][0][0]
        y=support[i][0][1]
        b=0
        q.append([])
        o=[x,y]
        for j in range(len(loads)):
            b=b-(loads[j][0][0]-x)*loads[j][1][1]+(loads[j][0][1]-y)*loads[j][1][0]
        d.append(b)
        for p in range(len(support)):
            for k in range(2):
                if support[p][3-k]!=0:
                    q[i].append(support[p][0][k]-o[k])

    t=i+1
    #Ny and Nx not in order (y 1st and then x)

    c1=0
    q.append([])
    for i in range(len(support)):
        for k in range(support[i][1]):

            if k%2==0 and support[i][3]==1:
                q[t].append(0)
                c1=1
            elif k%2!=0 and support[i][2]==1:
                q[t].append(1)
    if c1==1:
        sum1=0
        for i in range(len(loads)):
            sum1=sum1+loads[i][1][0]
        d.append(-sum1)
    else:
        q.pop(t)
        t=t-1


    t=t+1
    q.append([])
    c2=0
    for i in range(len(support)):
        for k in range(2):

            if k%2!=0 and support[i][2]==1:
                q[t].append(0)

            elif k%2==0 and support[i][3]==1:
                q[t].append(1)
                c2 = 1

    sum1=0
    if c2==1:
        for i in range(len(loads)):
            sum1=sum1+loads[i][1][1]
        d.append(-sum1)
    else:
        q.pop(t)
        t=t-1
    #qx=b
    o=len(d)-len(q[0])
    y=len(q[0])
    for i in range(len(q)):
        if i!=y:
            q[i].append(0)
        else:
            q[i].append(1)

    support_soln=linearsoln.linear_solve(q,d)
    load_with_supports=loads
    t=0
    for i in range(len(support)):
        o=[]
        for k in range(support[i][1]):
            if k==0 and support[i][3]==1 and support[i][2]==0:
                o.append(support_soln[k+t+i])
                o.append(0)
            elif k==0 and support[i][3]==1 and support[i][2]==1:
                o.append(support_soln[k + t + i])
                o.append(support_soln[k+1+t+i])
            elif k==0 and support[i][3]==0:
                o.append(0)
                o.append(support_soln[k + t + i])
        o.reverse()
        load_with_supports.append([support[i][0],o])
        t=t+k
    return(load_with_supports,support_soln)

def reaction_in_truss_new1(coord,mem,support,loads):

    Reactions=[]
    #to find b
    d=[]
    q=[]
    for i in range(len(support)):
        x=support[i][0][0]
        y=support[i][0][1]
        b=0
        q.append([])
        o=[x,y]
        for j in range(len(loads)):
            b=b-(loads[j][0][0]-x)*loads[j][1][1]+(loads[j][0][1]-y)*loads[j][1][0]
        d.append(b)
        for p in range(len(support)):
            for k in range(2):
                if support[p][3-k]!=0:
                    q[i].append(support[p][0][k]-o[k])

    t=i+1
    #Ny and Nx not in order (y 1st and then x)

    c1=0
    q.append([])
    for i in range(len(support)):
        for k in range(support[i][1]):

            if k%2==0 and support[i][3]==1:
                q[t].append(0)
                c1=1
            elif k%2!=0 and support[i][2]==1:
                q[t].append(1)
    if c1==1:
        sum1=0
        for i in range(len(loads)):
            sum1=sum1+loads[i][1][0]
        d.append(-sum1)
    else:
        q.pop(t)
        t=t-1


    t=t+1
    q.append([])
    c2=0
    for i in range(len(support)):
        for k in range(2):

            if k%2!=0 and support[i][2]==1:
                q[t].append(0)

            elif k%2==0 and support[i][3]==1:
                q[t].append(1)
                c2 = 1

    sum1=0
    if c2==1:
        for i in range(len(loads)):
            sum1=sum1+loads[i][1][1]
        d.append(-sum1)
    else:
        q.pop(t)
        t=t-1
    #qx=b
    o=len(d)-len(q[0])
    y=len(q[0])
    for i in range(len(q)):
        if i!=y:
            q[i].append(0)
        else:
            q[i].append(1)

    support_soln=linearsoln.linear_solve(q,d)
    load_with_supports=loads

    t=0
    for i in range(len(support)):
        print('support no '+str(i+1))
        o=[]
        for k in range(support[i][1]):
            if k==0 and support[i][3]==1 and support[i][2]==0:
                print('value of Ny= ',end='')
                o.append(support_soln[k+t+i])
                o.append(0)
            elif k==0 and support[i][3]==1 and support[i][2]==1:
                print('value of Ny= ', end='')
                o.append(support_soln[k + t + i])
                o.append(support_soln[k+1+t+i])
            elif k==0 and support[i][3]==0:
                print('value of Nx= ',end='')
                o.append(0)
                o.append(support_soln[k + t + i])
            elif k==1:
                print('value of Nx= ',end='')
            print(support_soln[i + k + t])
        o.reverse()
        load_with_supports.append([support[i][0],o])
        t=t+k
        functional_support_soln=[]
        for i in range(len(support)):
            functional_support_soln.append([support[i][0],[support_soln[2*i],support_soln[2*i+1]]])
    return(load_with_supports,support_soln,functional_support_soln)


def reaction_in_truss_new1_wop(coord,mem,support,loads):

    Reactions=[]
    #to find b
    d=[]
    q=[]
    for i in range(len(support)):
        x=support[i][0][0]
        y=support[i][0][1]
        b=0
        q.append([])
        o=[x,y]
        for j in range(len(loads)):
            b=b-(loads[j][0][0]-x)*loads[j][1][1]+(loads[j][0][1]-y)*loads[j][1][0]
        d.append(b)
        for p in range(len(support)):
            for k in range(2):
                if support[p][3-k]!=0:
                    q[i].append(support[p][0][k]-o[k])

    t=i+1
    #Ny and Nx not in order (y 1st and then x)

    c1=0
    q.append([])
    for i in range(len(support)):
        for k in range(support[i][1]):

            if k%2==0 and support[i][3]==1:
                q[t].append(0)
                c1=1
            elif k%2!=0 and support[i][2]==1:
                q[t].append(1)
    if c1==1:
        sum1=0
        for i in range(len(loads)):
            sum1=sum1+loads[i][1][0]
        d.append(-sum1)
    else:
        q.pop(t)
        t=t-1


    t=t+1
    q.append([])
    c2=0
    for i in range(len(support)):
        for k in range(2):

            if k%2!=0 and support[i][2]==1:
                q[t].append(0)

            elif k%2==0 and support[i][3]==1:
                q[t].append(1)
                c2 = 1

    sum1=0
    if c2==1:
        for i in range(len(loads)):
            sum1=sum1+loads[i][1][1]
        d.append(-sum1)
    else:
        q.pop(t)
        t=t-1
    #qx=b
    o=len(d)-len(q[0])
    y=len(q[0])
    for i in range(len(q)):
        if i!=y:
            q[i].append(0)
        else:
            q[i].append(1)

    support_soln=linearsoln.linear_solve(q,d)
    load_with_supports=loads

    t=0
    for i in range(len(support)):
        o=[]
        for k in range(support[i][1]):
            if k==0 and support[i][3]==1 and support[i][2]==0:

                o.append(support_soln[k+t+i])
                o.append(0)
            elif k==0 and support[i][3]==1 and support[i][2]==1:
                o.append(support_soln[k + t + i])
                o.append(support_soln[k+1+t+i])
            elif k==0 and support[i][3]==0:

                o.append(0)
                o.append(support_soln[k + t + i])

        o.reverse()
        load_with_supports.append([support[i][0],o])
        t=t+k
        functional_support_soln=[]
        for i in range(len(support)):
            functional_support_soln.append([support[i][0],[support_soln[2*i],support_soln[2*i+1]]])
    return(load_with_supports,support_soln,functional_support_soln)

