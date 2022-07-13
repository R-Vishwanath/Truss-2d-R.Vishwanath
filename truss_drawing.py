import truss_details as td

def truss_drawing(coord,new_coord,mem,support,load_details):
    import turtle
    screen=turtle.Screen()
    screen.bgcolor('light green')
    tr=turtle.Turtle()
    tr.pencolor('blue')
    tr.pensize(5)
    sf=7
    tr.speed(0)
    for i in range(len(mem)):
        tr.penup()
        p1=coord[mem[i][0]-1]
        tr.goto(sf*p1[0],sf*p1[1])
        tr.pendown()
        p2 = coord[mem[i][1] - 1]
        tr.goto(sf*p2[0],sf* p2[1])
    print(support)
    for i in range(len(support)):
        if support[i][1]==2:
            tr.pencolor('black')
            tr.penup()
            p1 = support[i][0]
            tr.goto(sf * p1[0], sf * p1[1])
            tr.pendown()
            tr.goto(sf*(p1[0]-1.5),sf*(p1[1]-1.5))
            tr.goto(sf*(p1[0]+1.5),sf*(p1[1]-1.5))
            tr.goto(sf * p1[0], sf * p1[1])
        elif support[i][1]==1:
            tr.pencolor('black')
            tr.penup()
            p1 = support[i][0]
            tr.goto(sf * p1[0], sf * p1[1])
            tr.pendown()
            tr.goto(sf*(p1[0]-1.5),sf*(p1[1]-1.5))
            tr.goto(sf*(p1[0]+1.5),sf*(p1[1]-1.5))
            tr.goto(sf * p1[0], sf * p1[1])
            tr.penup()
            tr.goto(sf * p1[0], sf * p1[1]-2)
            tr.pendown()
            tr.circle(sf)
    tr.pensize(2)
    for i in range(len(load_details)):
        tr.penup()
        x=sf*load_details[i][0][0]
        y=sf*load_details[i][0][1]
        tr.goto(x,y)
        tr.pendown()
        if int(load_details[i][1][0])<0:
            tr.color('orange')
            tr.goto(-50+x,y)
            tr.goto(x-40,y+10)
            tr.goto(x-40,y-10)
            tr.goto(-50+x,y)
        elif int(load_details[i][1][0])>0:
            tr.color('yellow')
            tr.goto(50+x,y)
            tr.goto(x+40,y+10)
            tr.goto(x+40,y-10)
            tr.goto(50+x,y)
        tr.penup()
        tr.goto(x, y)
        tr.pendown()
        if int(load_details[i][1][1])<0:
            tr.color('violet')
            tr.goto(x,y-50)
            tr.goto(x+10,y-40)
            tr.goto(x-10,y-40)
            tr.goto(x,y-50)
        elif int(load_details[i][1][1])>0:
            tr.color('purple')
            tr.goto(x,50+y)
            tr.goto(x+10,y+40)
            tr.goto(x-10,y+40)
            tr.goto(x,y+50)


    tr.pencolor('grey')
    tr.pensize(3)

    tr.speed(0)
    for i in range(len(mem)):
        tr.penup()
        p1 = new_coord[mem[i][0] - 1]
        tr.goto(sf * p1[0], sf * p1[1])
        tr.pendown()
        p2 = new_coord[mem[i][1] - 1]
        tr.goto(sf * p2[0], sf * p2[1])


    turtle.done()


def truss_drawing_w_D(coord,D,mem,support,load_details):
    import turtle
    new_coord = []
    for i in range(len(coord)):
        new_coord.append([coord[i][0] + D[i][0], coord[i][1] + D[i][1]])
    return new_coord
    screen=turtle.Screen()
    screen.bgcolor('light green')
    tr=turtle.Turtle()
    tr.pencolor('blue')
    tr.pensize(5)
    sf=7
    tr.speed(0)
    for i in range(len(mem)):
        tr.penup()
        p1=coord[mem[i][0]-1]
        tr.goto(sf*p1[0],sf*p1[1])
        tr.pendown()
        p2 = coord[mem[i][1] - 1]
        tr.goto(sf*p2[0],sf* p2[1])
    for i in range(len(support)):
        if support[i][1]==2:
            tr.pencolor('black')
            tr.penup()
            p1 = support[i][0]
            tr.goto(sf * p1[0], sf * p1[1])
            tr.pendown()
            tr.goto(sf*(p1[0]-1.5),sf*(p1[1]-1.5))
            tr.goto(sf*(p1[0]+1.5),sf*(p1[1]-1.5))
            tr.goto(sf * p1[0], sf * p1[1])
        elif support[i][1]==1:
            tr.pencolor('black')
            tr.penup()
            p1 = support[i][0]
            tr.goto(sf * p1[0], sf * p1[1])
            tr.pendown()
            tr.goto(sf*(p1[0]-1.5),sf*(p1[1]-1.5))
            tr.goto(sf*(p1[0]+1.5),sf*(p1[1]-1.5))
            tr.goto(sf * p1[0], sf * p1[1])
            tr.penup()
            tr.goto(sf * p1[0], sf * p1[1]-2)
            tr.pendown()
            tr.circle(sf)
    tr.pensize(2)
    for i in range(len(load_details)):
        tr.penup()
        x=sf*load_details[i][0][0]
        y=sf*load_details[i][0][1]
        tr.goto(x,y)
        tr.pendown()
        if int(load_details[i][1][0])<0:
            tr.color('orange')
            tr.goto(-50+x,y)
            tr.goto(x-40,y+10)
            tr.goto(x-40,y-10)
            tr.goto(-50+x,y)
        elif int(load_details[i][1][0])>0:
            tr.color('yellow')
            tr.goto(50+x,y)
            tr.goto(x+40,y+10)
            tr.goto(x+40,y-10)
            tr.goto(50+x,y)
        tr.penup()
        tr.goto(x, y)
        tr.pendown()
        if int(load_details[i][1][1])<0:
            tr.color('violet')
            tr.goto(x,y-50)
            tr.goto(x+10,y-40)
            tr.goto(x-10,y-40)
            tr.goto(x,y-50)
        elif int(load_details[i][1][1])>0:
            tr.color('purple')
            tr.goto(x,50+y)
            tr.goto(x+10,y+40)
            tr.goto(x-10,y+40)
            tr.goto(x,y+50)


    tr.pencolor('grey')
    tr.pensize(3)

    tr.speed(0)
    for i in range(len(mem)):
        tr.penup()
        p1 = new_coord[mem[i][0] - 1]
        tr.goto(sf * p1[0], sf * p1[1])
        tr.pendown()
        p2 = new_coord[mem[i][1] - 1]
        tr.goto(sf * p2[0], sf * p2[1])


    turtle.done()