# whenever you make a turtle, do import turtle
import turtle
# simple commmands:
# bob.forward(100) # this makes the cursor go forward by 100 pixels
# bob.left(45) # this makes bob face to the left by 45 degrees
# bob.right(90) # this makes bob face to the right by 90 degrees
bob = turtle.Turtle() # this create the turtle cursor
bob.color("blue", "red") # this sets the color. the 1st is the outline, 2nd is the inside

bob.begin_fill()
bob.forward(50)
bob.left(90)
bob.forward(50)
bob.left(90)
bob.forward(50)
bob.left(90)
bob.forward(50)
bob.end_fill()

print('this code is running. close the turtle graphics app to end it')




turtle.done() # this finishes the code
