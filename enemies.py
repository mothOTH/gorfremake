from turtle import Turtle


class BasicDude(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.ht()
        self.fillcolor("green")
        self.penup()
        self.speed(10)
        self.setheading(270)


class EnemyBlock(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.shapesize(stretch_wid=4.5, stretch_len=11)
        self.shape("square")
        self.goto(-30, 165)
        self.color("white")
