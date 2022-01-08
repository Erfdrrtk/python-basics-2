# whenever you make a turtle, do import turtle
import turtle
# simple commmands:
# bob.forward(100) # this makes the cursor go forward by 100 pixels
# bob.left(45) # this makes bob face to the left by 45 degrees
# bob.right(90) # this makes bob face to the right by 90 degrees
def boxes():
    bob = turtle.Turtle() # this create the turtle cursor
    bob.color("blue", "red") # this sets the color. the 1st is the outline, 2nd is the inside
    # this part is responsible for drawing the boxes:
    bob.begin_fill()
    bob.forward(100)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(100)
    bob.end_fill()
    # this allows the cursor to move without drawing anything
    bob.penup()
    bob.forward(100)
    bob.pendown()
# this creates a 2nd box
    bob.begin_fill()
    bob.forward(100)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(100)
    bob.end_fill()
    # do boxes() to run this piece of code





def face():
    #the left eye
    cat = turtle.Turtle()
    cat.speed(1)
    cat.color("blue", "green")
    cat.penup()
    cat.left(90)
    cat.forward(100)
    cat.left(90)
    cat.forward(100)

    cat.pendown()
    cat.begin_fill()
    cat.forward(100)
    cat.right(90)
    cat.forward(100)
    cat.right(90)
    cat.forward(100)
    cat.right(90)
    cat.forward(100)
    cat.end_fill()
    # the right eye
    cat.color("pink", "blue")
    cat.penup()
    cat.left(90)
    cat.forward(200)
    cat.pendown()
    cat.begin_fill()
    cat.forward(100)
    cat.left(90)
    cat.forward(100)
    cat.left(90)
    cat.forward(100)
    cat.left(90)
    cat.forward(100)
    cat.end_fill()

# the mouth
    cat.color("green", "black")
    cat.penup()
    cat.forward(300)
    cat.left(90)
    cat.pendown()
    cat.begin_fill()
    cat.forward(100)
    cat.left(90)
    cat.forward(100)
    cat.left(90)
    cat.forward(400)
    cat.left(90)
    cat.forward(100)
    cat.left(90)
    cat.forward(400)
    cat.left(90)
    cat.forward(100)
    cat.end_fill()
    # the ends of the mouth
    cat.color("cyan", "red")
    cat.begin_fill()
    cat.forward(80)
    cat.right(90)
    cat.forward(100)
    cat.right(90)
    cat.forward(80)
    cat.right(90)
    cat.forward(100)

    cat.end_fill()
    cat.penup()
    cat.forward(150)
    cat.right(90)
    cat.forward(50)
    cat.pendown()
    # the nose
    cat.color("green", "purple")
    cat.begin_fill()
    cat.forward(50)
    cat.left(90)
    cat.forward(100)
    cat.left(90)
    cat.forward(50)
    cat.left(90)
    cat.forward(100)
    cat.end_fill()

    cat.penup()
    cat.right(90)
    cat.forward(50)
    cat.right(90)
    cat.forward(250)
    cat.right(90)

    # the other mouth end
    cat.pendown()
    cat.color("brown", "orange")
    cat.begin_fill()
    cat.forward(80)
    cat.left(90)
    cat.forward(100)
    cat.left(90)
    cat.forward(80)
    cat.left(90)
    cat.forward(100)
    cat.end_fill()

face()










turtle.done() # this finishes the code
