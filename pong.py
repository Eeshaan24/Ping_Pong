import turtle
from winsound import SND_ASYNC
from playsound import playsound

from numpy import square

wn = turtle.Screen()
wn.title("Pong by Eeshaan")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # stops the window from updating.. if we dont do that things will run slower

#paddle A

paddle_a = turtle.Turtle()  #Turtle - class name
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()  #penup() basically makes sure that the moving object that you've created does not draw anything on the window. So if you have a ball and you want it to move around and draw anything on the window, then you use the penup()
paddle_a.goto(-350,0)

#paddle B

paddle_b = turtle.Turtle()  #Turtle - class name
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup() 
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()  #Turtle - class name
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup() 
ball.goto(0,0)
ball.dx = 0.05  # dx- delta or change.. basically speed
ball.dy = -0.05

#score
score_a = 0
score_b = 0

#pen - for writing scores
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0",  align = "center", font = ("courier", 24, "normal"))

#function

def paddle_a_up():
    y = paddle_a.ycor()  #ycor - comes from turtle module.. It gives y coordinate
    y = y + 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()  #ycor - comes from turtle module.. It gives y coordinate
    y = y - 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()  #ycor - comes from turtle module.. It gives y coordinate
    y = y + 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()  #ycor - comes from turtle module.. It gives y coordinate
    y = y - 20
    paddle_b.sety(y)

#keyboard
wn.listen()  #listens the inputs from keyboard
wn.onkeypress(paddle_a_up, "w") # when w pressed it calls function paddle_a_up
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#main game loop

while True:
    wn.update()  #everytime loop runs it updates the screen

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1   #changes the direction of speed
        #playsound('sound.wav', playsound.)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align = "center", font = ("courier", 24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align = "center", font = ("courier", 24, "normal"))


    #paddle and ball collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40): 
        ball.setx(-340)
        ball.dx *= -1


