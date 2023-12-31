# imported turtle module
import turtle
# form of screen
wind = turtle.Screen()
# title
wind.title("Ping Pong  by:sabry")
# color of background
wind.bgcolor("green")
# width and height
wind.setup(width=800, height=600)
# iam a controller and the screen not update without permission
wind.tracer(0)

# madrab1
madrab1 = turtle.Turtle()  # initialize turtle object
# speed
madrab1.speed(0)
# shape of madrab1
madrab1.shape("square")
# color of madrab1
madrab1.color("blue")
# shape size
madrab1.shapesize(stretch_wid=5, stretch_len=1)  # (5*20,1*20)
madrab1.penup()  # stop the object from drawing lines
# location of madrab1
madrab1.goto(-350, 0)

# madrab2
madrab2 = turtle.Turtle()  # initialize turtle object
# speed
madrab2.speed(0)
# shape of madrab2
madrab2.shape("square")
# color of madrab2
madrab2.color("red")
# shape size
madrab2.shapesize(stretch_wid=5, stretch_len=1)   # (5*20,1*20)
madrab2.penup()  # stop the object from drawing lines
# location of madrab2
madrab2.goto(350, 0)
# ball
ball = turtle.Turtle()  # initialize turtle object
# speed
ball.speed(0)
# shape of ball
ball.shape("circle")
# color of ball
ball.color("white")
# shape size
ball.penup()  # stop the object from drawing lines
# location of ball
ball.goto(0, 0)
ball.dx = 0.35
ball.dy = 0.35
# score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player 1: 0 & Player 2: 0",align="center",font=("courier",24," normal"))

# functions
def madrab1_up():
    y = madrab1.ycor()  # get the y coordinate of madrab1
    y = y+20    # increase y by 20
    madrab1.sety(y)     # change y to new y
def madrab1_down():
    y = madrab1.ycor()  # get the y coordinate of madrab1
    y = y-20    # decrease y by 20
    madrab1.sety(y)    # change y to new y

def madrab2_up():
    y = madrab2.ycor()   # get the y coordinate of madrab2
    y = y+20    # increase y by 20
    madrab2.sety(y)     # change y to new y
def madrab2_down():
    y = madrab2.ycor()   # get the y coordinate of madrab2
    y = y-20  # decrease y by 20
    madrab2.sety(y)     # change y to new y
# keyboard_bindings
# tell the window expect keyboard input
wind.listen()
wind.onkeypress(madrab1_up, "w")
wind.onkeypress(madrab1_down, "s")
wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")

# loop Screen
while True:
    wind.update()  # update the screen everytime the loop runs

    # move the ball
    ball.setx(ball.xcor()+ball.dx)  # ball starts at 0 and every time run loop>>>increase by 0.35
    ball.sety(ball.ycor()+ball.dy)  # ball starts at 0 and every time run loop>>>increase by 0.35

    # border check   top border +300px, bottom border -300 px and ball is 20 px
    if ball.ycor() > 290:   # if ball is at top border
        ball.sety(290)      # set y coordinate +290
        ball.dy *= -1       # reverse direction   +0.35>>>>-0.35

    if ball.ycor() < -290:   # if ball is at bottom border
        ball.sety(-290)       # set y coordinate -290
        ball.dy *= -1         # reverse direction   +0.35>>>>-0.35

    if ball.xcor() > 390:     # if ball is at right border
        ball.goto(0, 0)       # return to the center
        ball.dx *= -1         # reverse direction
        score1 += 1
        score.clear()
        score.write("Player 1: {} & Player 2: {}".format(score1, score2), align="center", font=("courier", 24, " normal"))

    if ball.xcor() < -390:    # if ball is at left border
        ball.goto(0, 0)       # return to the center
        ball.dx *= -1         # reverse direction
        score2 += 1
        score.clear()
        score.write("Player 1: {} & Player 2: {}".format(score1, score2), align="center", font=("courier", 24, " normal"))


# tasadm madrab1 with ball
    if (ball.xcor()>340 and ball.xcor()<350 ) and (ball.ycor()<madrab2.ycor()+40 and ball.ycor()>madrab2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1