import turtle


def go():
    pencil.forward(50)

def right():
    pencil.right(45)

def left():
    pencil.left(45)

def quite():
    wn.bye()

def thick():
    global thick_pen
    thick_pen += 5
    pencil.pensize(thick_pen)

def thin():
    global thick_pen
    thick_pen -= 5
    if thick_pen > 0:
        pencil.pensize(thick_pen)
        
    else:
        thick_pen = 1
        pencil.pensize(thick_pen)

def draw():
    global pen
    if pen == 1:
        pencil.penup()
        pen = 0
    else:
        pencil.pendown()
        pen = 1

def delete():
    global pen
    if pen == 1:
        pencil.pencolor('white')
        pen = 0
    else:
        pencil.pencolor('black')
        pen = 1

def color():
    global number
    colors=['blue','red','yellow','orange','green','brown','pink','grey','violet','black']
    number += 1
    if number==10:
        number = 0      
    pencil.pencolor(colors[number])

def text_menu(text, x, y):
    write = turtle.Turtle()
    write.hideturtle()
    write.penup()
    write.goto(x,y)
    write.write(text, font=12)
    
def main():
    global pencil
    global wn
    global thick_pen
    global pen
    global number
    thick_pen = 1
    pen = 1
    number = 0

   
    wn=turtle.Screen()
    wn.setup(500,700)
    wn.title('Draw Pencil')
    wn.bgcolor('white')
    
    text_menu("↑-oldinga yurg'izish", 400, 400)
    text_menu("→-o'nga yurg'izish", 400, 375)
    text_menu("←-chapga yurg'izish", 400, 350)
    text_menu("b-qalinlashtirish", 400, 325)
    text_menu("i-ingichkalashtirish", 400, 300)
    text_menu("space-chizishni to'xtatish va", 400, 275)
    text_menu("yana ishga tushirish", 400, 250)
    text_menu("q-chiqib ketish", 400, 225)
    text_menu("c-rangini o'zgartirish", 400, 200)
    text_menu("d-o'chirg'ich", 400, 175)

    
    pencil=turtle.Turtle()
    pencil.pensize(thick_pen)

    wn.onkey(go, 'Up')   
    wn.onkey(right, 'Right')
    wn.onkey(left, 'Left')
    wn.onkey(quite, 'q')
    wn.onkey(thick, 'b')
    wn.onkey(thin, 'i')
    wn.onkey(draw, 'space')
    wn.onkey(delete, 'd')
    wn.onkey(color, 'c')
    
    
    wn.listen()
    wn.mainloop()

    
main()
