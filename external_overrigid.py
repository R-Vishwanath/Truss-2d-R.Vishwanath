import just_rigid
import linearsoln
import truss_drawing
import Displacement_printing_coordinate_changing

def statically_indeterminate(mem,coord,support,loads,l,rxn):
    support_primary=[]
    w=0

    c11=0#check if atleast one roller
    un_updated_loads=list.copy(loads)
    og_supp=[]
    for i in range(len(support)):
        og_supp.append([])
        for j in range(len(support[i])):
            og_supp[i]=list.copy(support[i])


    for i in range(len(support)-1):
        for j in range(i+1,len(support)):
            if support[i][1]+support[j][1]==3:
                primary_reduntant1=i+1
                primary_reduntant2 =j+1
                support_primary.append(support[i])
                support_primary.append(support[j])
                w=1
                break
        if w==1:
            break

    if w!=1:
        support_primary.append(support[0])
        support_primary.append([support[len(support)-1][0],1,0,1])
        primary_reduntant1=1
        primary_reduntant2=len(support)
        support[len(support)-1][1]=1
        support[len(support)-1][3]=0
        support.append([support[len(support)-1][0],1,1,0])
        c11=1


    D_primary,n_primary=just_rigid.just_rigid_(mem,coord,support_primary,3,loads,l)
    D_primary_needed=[]

    for i in range(len(support)):
        if i!=primary_reduntant2-1 and i!=primary_reduntant1-1:
            for k in range(support[i][1]):
                coordcheck=support[i][0]
                for p in range(len(coord)):
                    if coord[p]==coordcheck:
                        break
                if support[i][1]==1:
                    if support[i][2]==1:
                        D_primary_needed.append(-D_primary[p][0])
                    else:
                        D_primary_needed.append(-D_primary[p][1])
                elif support[i][1]==2:
                    if k==0:
                        D_primary_needed.append(-D_primary[p][0])
                    else:
                        D_primary_needed.append(-D_primary[p][1])
    n_tot_redundant=[]
    #finding flexibility coeffiecients
    for i in range(len(support)):
        if i!=primary_reduntant2-1 and i!=primary_reduntant1-1:
            for k in range(support[i][1]):
                load_redundant = []
                if support[i][1]==1:
                    if support[i][2]==1:
                        load_redundant.append([support[i][0],[1,0]])
                        D_redundant, n_redundant = just_rigid.just_rigid_(mem, coord, support_primary, 3, load_redundant, l)
                        n_tot_redundant.append(n_redundant)
                        load_redundant.pop(0)
                    else:
                        load_redundant.append([support[i][0], [0, 1]])
                        D_redundant, n_redundant = just_rigid.just_rigid_(mem, coord, support_primary, 3, load_redundant, l)
                        n_tot_redundant.append(n_redundant)
                        load_redundant.pop(0)
                else:
                    if k==0:
                        load_redundant.append([support[i][0],[1,0]])
                        D_redundant, n_redundant = just_rigid.just_rigid_(mem, coord, support_primary, 3, load_redundant, l)
                        n_tot_redundant.append(n_redundant)
                        load_redundant.pop(0)
                    elif k==1:
                        load_redundant.append([support[i][0], [0, 1]])
                        D_redundant, n_redundant = just_rigid.just_rigid_(mem, coord, support_primary, 3, load_redundant, l)
                        n_tot_redundant.append(n_redundant)
                        load_redundant.pop(0)
    f=[]
    E = 2 * pow(10, 5)
    A = 5 * pow(10, -3)
    for i in range(len(n_tot_redundant)):
        f.append([])
        for j in range(len(n_tot_redundant)):
            sum=0
            for k in range(len(mem)):
                sum=sum+n_tot_redundant[i][k]*n_tot_redundant[j][k]*l[k]/(E*A)
            f[i].append(sum)
    support_soln = linearsoln.linear_solve(f, D_primary_needed)
    new_coord=coord
    modified_loads=[]
    u=0
    for i in range(len(support)):
        if i!=primary_reduntant2-1 and i!=primary_reduntant1-1:
            r1=[]
            for k in range(support[i][1]):
                load_redundant = []
                if support[i][1]==1:
                    if support[i][2]==1:
                        modified_loads.append([support[i][0],[support_soln[u],0]])
                    else:
                        modified_loads.append([support[i][0],[0,support_soln[u]]])
                else:
                    if k==0:
                        r1.append(support_soln[u])
                    elif k==1:
                        r1.append(support_soln[u])
                        modified_loads.append([support[i][0],r1])
                u+=1
    if c11!=1:
        for i in range(len(modified_loads)):
            un_updated_loads.append(modified_loads[i])
        D,n,support_soln=just_rigid.just_rigid_with_p_for_origid(mem,coord,support_primary,3,un_updated_loads,l,modified_loads,og_supp)
        new_coord=Displacement_printing_coordinate_changing.new_coordinates(coord,D)
        ki=support_soln[len(support_soln)-1][0]
    #support_soln[len(support_soln)-2][1][1]=support_soln[len(support_soln)-1][1][0]
    #support_soln.pop(len(support_soln)-1)
    else:
        for i in range(len(modified_loads)):
            un_updated_loads.append(modified_loads[i])
        D,n,support_soln=just_rigid.just_rigid_without_p_for_origid(mem,coord,support_primary,3,un_updated_loads,l,modified_loads,og_supp)
        new_coord=Displacement_printing_coordinate_changing.new_coordinates(coord,D)
        ki=support_soln[len(support_soln)-1][0]
    for i in range(len(modified_loads)):
        support_soln.append(modified_loads[i])
    ckey=0
    if c11==1:
        for i in range(len(support_soln)):
            for j in range(i+1,len(support_soln)):
                if support_soln[i][0]==support_soln[j][0]:
                    support_soln[i][1][1]=support_soln[j][1][0]
                    support_soln.pop(j)
                    ckey=1
                    break
            if ckey==1:
                break

    return(D,new_coord,n,support_soln)
    #truss_drawing.truss_drawing(coord,new_coord,mem,support,loads)






