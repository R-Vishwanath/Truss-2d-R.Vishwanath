import printer_for_supports
import truss_details as td
import truss_drawing
import load_details
import linearsoln
import printing_redundants
import reaction_Truss
import axialforce
import displacement_find
import lengthmember
import Displacement_printing_coordinate_changing

def just_rigid_(mem,coord,support,rxn,loads,l,E,A):
    if rxn==3:
        load_with_supports,support_soln=reaction_Truss.reaction_in_truss_wop(coord,mem,support,loads)
        n=axialforce.axial_force_wop(coord,mem,load_with_supports,support_soln)
        D=displacement_find.displacement_(n,coord,mem,support,l,E,A)
        new_coord=Displacement_printing_coordinate_changing.new_coordinates(coord,D)
    return (D,n)

def just_rigid_with_p(mem,coord,support,rxn,loads,l):
    if rxn==3:
        load_with_supports,support_soln=reaction_Truss.reaction_in_truss(coord,mem,support,loads)
        n=axialforce.axial_force(coord,mem,load_with_supports,support_soln)
        D=displacement_find.displacement_(n,coord,mem,support,l)
        Displacement_printing_coordinate_changing.printing_displacement(D)
        new_coord=Displacement_printing_coordinate_changing.new_coordinates(coord,D)
    return (D,n)

def just_rigid_with_p_for_origid(mem,coord,support,rxn,loads,l,modified_loads,og_supp,E,A):
    if rxn==3:
        load_with_supports,support_soln,functional_support_soln=reaction_Truss.reaction_in_truss_new1_wop(coord,mem,support,loads)#have to edit support soln
        printing_redundants.printing_redundants_(coord,og_supp, modified_loads,functional_support_soln)
        n=axialforce.axial_force(coord,mem,load_with_supports,support_soln)
        D=displacement_find.displacement_(n,coord,mem,support,l,E,A)
        Displacement_printing_coordinate_changing.printing_displacement(D)
        new_coord=Displacement_printing_coordinate_changing.new_coordinates(coord,D)
    return (D,n,functional_support_soln)

def just_rigid_without_p_for_origid(mem,coord,support,rxn,loads,l,modified_loads,og_supp,E,A):
    if rxn==3:
        load_with_supports,support_soln,functional_support_soln=reaction_Truss.reaction_in_truss_new1_wop(coord,mem,support,loads)#have to edit support soln
        ckey=0
        for i in range(len(functional_support_soln)):
            for j in range(len(modified_loads)):
                if functional_support_soln[i][0] == modified_loads[j][0]:
                    functional_support_soln[i][1][1] = modified_loads[j][1][0]
                    ckey = 1
                    break
            if ckey == 1:
                break
        printer_for_supports.printer(coord,functional_support_soln,og_supp)
        n=axialforce.axial_force(coord,mem,load_with_supports,support_soln)
        D=displacement_find.displacement_(n,coord,mem,support,l,E,A)
        Displacement_printing_coordinate_changing.printing_displacement(D)
        new_coord=Displacement_printing_coordinate_changing.new_coordinates(coord,D)
    return (D,n,functional_support_soln)