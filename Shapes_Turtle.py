def triangle(color,width,length):
    import turtle
    s=turtle.Screen()
    t=turtle.Turtle()

    t.color(color)
    t.width(width)

    for i in range (3):
        t.fd(length)
        t.left(120)

def square(color,width,length):
    import turtle
    s=turtle.Screen()
    t=turtle.Turtle()
    
    t.color(color)
    t.width(width)

    for i in range(4):
        t.fd(length)
        t.left(90)

def line(color,width,length):
    import turtle
    s=turtle.Screen()
    t=turtle.Turtle()

    t.color(color)
    t.width(width)
    t.fd(length)

shape=input("Enter shape")
if shape=="triangle":
    triangle(input("Enter color"), int(input("Enter width")), int(input("Enter length")))
elif shape=="square":
    square(input("Enter color"), int(input("Enter width")), int(input("Enter length")))
elif shape=="line":
    line(input("Enter color"), int(input("Enter width")), int(input("Enter length")))

