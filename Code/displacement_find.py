import reaction_Truss
import axialforce
import internal_overrigid
import math
def displacement_(n,coord,mem,support,l,E,A):
    D=[]
    for q in range(len(coord)):
        loads=[]
        sno=q+1
        for i in range(len(coord)):
            if i==sno-1:
                loads.append([coord[i],[1,0]])
            else:
                loads.append([coord[i],[0,0]])
        load_with_supports,support_soln=reaction_Truss.reaction_in_truss_wop(coord,mem,support,loads)
        nx1=axialforce.axial_force_wop(coord, mem, load_with_supports, support_soln)
        sum=0
        for i in range(len(mem)):
            sum=sum+nx1[i]*n[i]*l[i]/(E[i]*A[i])# 9*-6 for E and A and 6 as nx1 and n in KN
        x1=sum
        loads=[]
        for i in range(len(coord)):
            if i==sno-1:
                loads.append([coord[i],[0,1]])
            else:
                loads.append([coord[i],[0,0]])
        load_with_supports, support_soln=reaction_Truss.reaction_in_truss_wop(coord,mem,support,loads)
        nx1=axialforce.axial_force_wop(coord, mem, load_with_supports, support_soln)
        sum=0
        for i in range(len(mem)):
            sum=sum+nx1[i]*n[i]*l[i]/(E[i]*A[i])
        y1=sum

        D.append([round(x1,3),round(y1,3)])
    return D

def displacement_i_o_rigid(n,coord,mem,support,l,E,A):
    D=[]
    ol = []
    for i in range(len(support)):
        ol.append(support[i][0])
    for q in range(len(coord)):
        loads1=[]
        sno=q+1
        ol=[]
        for i in range(len(coord)):
            if i==sno-1:
                loads1.append([coord[i], [1, 0]])
            else:
                loads1.append([coord[i], [0, 0]])

        nx1=internal_overrigid.statically_indeterminate_wop( mem,coord,support,loads1,l,E,A)
        sum=0
        for i in range(len(mem)):
            sum=sum+nx1[i]*n[i]*l[i]/(E[i]*A[i])
        x1=sum


        loads1=[]
        for i in range(len(coord)):
            if i==sno-1:
                loads1.append([coord[i], [0, 1]])
            else:
                loads1.append([coord[i], [0, 0]])
        load_with_supports, support_soln=reaction_Truss.reaction_in_truss_wop(coord, mem, support, loads1)
        nx1=internal_overrigid.statically_indeterminate_wop( mem,coord,support,loads1,l,E,A)
        sum=0
        for i in range(len(mem)):
            sum=sum+nx1[i]*n[i]*l[i]/(E[i]*A[i])
        y1=sum
        D.append([round(x1,3),round(y1,3)])
    return D