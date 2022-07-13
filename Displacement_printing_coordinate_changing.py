def printing_displacement(D):
    for i in range(len(D)):
        print('For joint '+str(i+1))
        print('X displacement : '+ str(D[i][0]))
        print('Y displacement : ' +str(D[i][1]))

def new_coordinates(coord,D):
    new_coord=[]
    for i in range(len(coord)):
        new_coord.append([coord[i][0]+D[i][0],coord[i][1]+D[i][1]])
    return new_coord