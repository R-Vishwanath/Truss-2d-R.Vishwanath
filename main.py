import truss_details as td
import truss_drawing
import load_details
import external_overrigid
import linearsoln
import reaction_Truss
import axialforce
import displacement_find
import lengthmember
import Displacement_printing_coordinate_changing
import internal_overrigid
k=td.truss_det()
coord=k[0]
mem=k[1]
support=k[2]
rxn=k[3]
loads=load_details.loadetails(coord)
loads_new=list.copy(loads)
l = lengthmember.length_mem(mem, coord)

if rxn==3:
    if len(mem)+3<=2*len(coord):
        load_with_supports,support_soln=reaction_Truss.reaction_in_truss(coord,mem,support,loads)
        n=axialforce.axial_force(coord,mem,load_with_supports,support_soln)
        print('\n')
        print('Displacement Calculations')
        D=displacement_find.displacement_(n,coord,mem,support,l)
        Displacement_printing_coordinate_changing.printing_displacement(D)
        new_coord=Displacement_printing_coordinate_changing.new_coordinates(coord,D)
        #print(new_coord)
        truss_drawing.truss_drawing(coord,new_coord,mem,support,loads)
    elif len(mem) + 3 > 2 * len(coord):
        load_with_supports, support_soln = reaction_Truss.reaction_in_truss(coord, mem, support, loads)
        n=internal_overrigid.statically_indeterminate(mem,coord,support,loads,l)
        D = displacement_find.displacement_i_o_rigid(n, coord, mem, support, l)
        Displacement_printing_coordinate_changing.printing_displacement(D)
        new_coord=Displacement_printing_coordinate_changing.new_coordinates(coord,D)
        truss_drawing.truss_drawing(coord, new_coord, mem, support, loads_new)
        #to find displacement for internally over rigid strucutres
elif rxn<3:
    print('unstable')
else:
    D,new_coord,n,support_soln=external_overrigid.statically_indeterminate(mem,coord,support,loads,l,rxn)
    truss_drawing.truss_drawing(coord, new_coord, mem, support, loads_new)




