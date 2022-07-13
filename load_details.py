import turtle
def loadetails(coord):
    n=int(input('number of loads'))
    loads=[]
    for i in range(n):
        print('For load no ' + str(i + 1))
        p=int(input('coordinate number'))
        q=float(input('magnitude of force in x direction'))
        r=float(input('magnitude of force in y direction'))
        loads.append([coord[p-1],[q,r]])
    return loads
