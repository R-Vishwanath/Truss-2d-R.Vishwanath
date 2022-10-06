def printing_redundants_(coord,support,modified_loads,support_soln):
    l=[]
    c=0
    u_support_soln=[]
    for i in range(len(coord)):
        d=0
        for j in range(len(support_soln)):
            if coord[i]==support_soln[j][0]:
                u_support_soln.append(support_soln[j])
                d==1
        if d!=1:
            for k in range(len(modified_loads)):
                if coord[i]==modified_loads[k][0]:
                    u_support_soln.append(modified_loads[k])
    print(u_support_soln)

    for i in range(len(support)):
        print('support no ' + str(i + 1))
        o = []
        for k in range(support[i][1]):
            if k == 0 and support[i][3] == 1 and support[i][2] == 0:
                print('value of Ny= ', end='')
                o.append(u_support_soln[i][1][1 - k])
                o.append(0)
            elif k == 0 and support[i][3] == 1 and support[i][2] == 1:
                print('value of Ny= ', end='')
                o.append(u_support_soln[i][1][1 - k])
                o.append(u_support_soln[i][1][k])
            elif k == 0 and support[i][3] == 0:
                print('value of Nx= ', end='')
                o.append(0)
                o.append(u_support_soln[i][1][1 - k])
            elif k == 1:
                print('value of Nx= ', end='')
            print(u_support_soln[i][1][1 - k])
