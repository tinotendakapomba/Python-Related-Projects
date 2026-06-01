import turtle
# this game is designed by Tinotenda Kapomba 
# you dont have permissionto destribute the game or any part of the games code wihout the owner permission
window = turtle.Screen()
window.title("pong game by Tinotenda Kapomba")
window.bgcolor("black")
window.setup(width = 800 , height = 600)
window.tracer(0)

#paddle_a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid= 5,  stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle_b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid= 5,  stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.7
ball.dy = 0.7

# function
def paddle_a_up ():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety (y)


def paddle_a_down ():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety (y)
 
def paddle_b_up ():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety (y)


def paddle_b_down ():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety (y)
 
 # keyboard binding
window.listen()
window.onkeypress (paddle_a_up,"w")
window.onkeypress (paddle_a_down,"s")
window.onkeypress (paddle_b_up,"Up")
window.onkeypress (paddle_b_down,"Down")





#Main game loop

while True:
    window.update()

    # moving ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1


    #paddle and ball collision

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx *=-1

    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx *=-1
        