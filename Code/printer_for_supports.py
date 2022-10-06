def printer(coord,support_soln,support):
    u_support_soln=[]

    for i in range(len(coord)):
        for j in range(len(support_soln)):
            if coord[i]==support_soln[j][0]:
                u_support_soln.append(support_soln[j])
    t=0

    for i in range(len(support)):
        print('support no '+str(i+1))
        o=[]
        for k in range(support[i][1]):
            if k==0 and support[i][3]==1 and support[i][2]==0:
                print('value of Ny= ',end='')
                o.append(u_support_soln[i][1][1-k])
                o.append(0)
            elif k==0 and support[i][3]==1 and support[i][2]==1:
                print('value of Ny= ', end='')
                o.append(u_support_soln[i][1][1-k])
                o.append(u_support_soln[i][1][k])
            elif k==0 and support[i][3]==0:
                print('value of Nx= ',end='')
                o.append(0)
                o.append(u_support_soln[i][1][1-k])
            elif k==1:
                print('value of Nx= ',end='')
            print(u_support_soln[i][1][1-k])