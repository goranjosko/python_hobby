import turtle, tkinter, random
import time as t

t_pen = turtle.Turtle(visible=False)
t_screen = turtle.Screen()
t_screen.title('Turtle random test')

t_screen.tracer(False)
t_pen.hideturtle()
t_pen.pen(fillcolor="black", pencolor="#3d3a36", pensize=2)

# if I ever need message below maze/lab
def text(message,x,y,size):
    FONT = ('HoboStd', size, 'normal')
    t_pen.penup()
    t_pen.goto(x,y)    		  
    t_pen.write(message, align="left", font=FONT)

# box for writing box
def box(intDim, color):
    t_pen.begin_fill()
    t_pen.fillcolor(color)
    t_pen.forward(intDim)
    t_pen.left(90)
    # 90 deg.
    t_pen.forward(intDim)
    t_pen.left(90)
    # 180 deg.
    t_pen.forward(intDim)
    t_pen.left(90)
    # 270 deg.
    t_pen.forward(intDim)
    t_pen.end_fill()
    t_pen.setheading(0)
    t_pen.getscreen().update()

def t_loop(lab, node = None, special_call = None):
    # colors = { 
    #     0: '#ff6200', 
    #     1: '#ffa200', 
    #     2: '#ff2200', 
    #     4: '#888888', 
    #     9: '#525252'
    # }    
    colors = ['#ffffff', '#0C0F12', '#ff2200', '#FF0000', '#525252', '#ffb34f']
    t_pen.up()
    number_b = len(lab)
    box_size = 30
    x = - (number_b / 2) * box_size
    y = (number_b / 2) * box_size
    t_pen.setpos(x, y)
    t1 = t.time()
    if node:
        row, col = node[0], node[1]
        x = x + col * box_size
        y = y - row * box_size
        t_pen.setpos(x, y)
        t_pen.down()
        box(box_size, colors[lab[row][col]])
        t_pen.up()
    else:
        for i, b_row in enumerate(lab):
            for b_col in b_row:
                t_pen.down()
                box(box_size, colors[b_col])
                x += box_size
                t_pen.up()
                t_pen.setpos(x, y)
            b_col = 0
            y -= box_size
            x -= box_size * number_b
            t_pen.up()
            t_pen.setpos(x, y)

path = []

def lab_solver(lab, row, col):
    global path
    if lab[row][col] == 3:
        print(f'PATH {path}')
        return lab
    else:
        pos = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]
        for node in random.sample(pos, len(pos)):
            x, y = node[0], node[1]
            if (len(lab) - 1 >= x >= 0) and (len(lab) - 1 >= y >= 0):
                if lab[x][y] == 0:
                    lab[row][col] = 2
                    if (row, col) not in path:
                        path.append((row, col))
                    path.append((x, y))
                    t.sleep(0)
                    t_screen.ontimer(t_loop(lab, (row, col)), 10)
                    return lab_solver(lab, x, y)
                elif lab[x][y] == 3:
                    lab[row][col] = 2
                    path.append((x, y))
                    t_screen.ontimer(t_loop(lab, (row, col)), 10)
                    return lab_solver(lab, x, y)
        if len(path) == 0:
            return lab
        else:
            x, y = path.pop(-1)
            lab[x][y] = 4
            t_screen.ontimer(t_loop(lab, (x, y)), 10)
            return lab_solver(lab, x, y)

# number 3 represent goal!!
with open('lab_1.txt', 'r') as file:
    lab_data = file.read()
templist = []
lab = []
for line in lab_data.splitlines():
    for number in line:
        templist.append(int(number))
    lab.append(templist)
    templist = []

# uncomment this if you don't want to load external file with lab data
# lab = [
#     [1,1,0,0,0,0,1,3],
#     [0,1,1,1,0,1,1,0],
#     [0,1,1,1,0,1,0,0],
#     [0,0,0,0,1,1,0,1],
#     [0,1,1,1,1,1,0,0],
#     [0,0,0,0,1,0,1,0],
#     [0,1,1,0,1,0,0,0],
#     [0,1,1,0,0,0,1,0]
#     ]

t_loop(lab)
# function need lab (maze) matrix and starting position - row and column
a = lab_solver(lab, 0, 15)
t_screen.mainloop()