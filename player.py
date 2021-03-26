from turtle import Turtle

STARTING_POSITION = (0, -200)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.shape("turtle")
        self.fillcolor("white")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(0)
        self.tilt(90)
        self.showturtle()

    def move_left(self):
        if self.xcor() < -290:
            return
        else:
            self.bk(10)

    def move_right(self):
        if self.xcor() > 290:
            return
        else:
            self.fd(10)

    def new_guy(self, lives):
        self.ht()
        self.shape("turtle")
        self.goto(STARTING_POSITION)


class Missile(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=.5)
        self.fillcolor("purple")
        self.penup()
        self.speed(8)

    def destruction(self):
        self.ht()
        self.goto(0, -200)

    def shoot(self):
        self.fd(15)
        self.showturtle()
