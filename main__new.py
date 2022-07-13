import truss_details as td
import truss_drawing
import load_details
import linearsoln
import reaction_Truss
import axialforce
import displacement_find
k=td.truss_det()
coord=k[0]
mem=k[1]
support=k[2]

loads=load_details.loadetails(coord)
load_with_supports,support_soln=reaction_Truss.reaction_in_truss(coord,mem,support,loads)
n=axialforce.axial_force(coord,mem,load_with_supports,support_soln)
