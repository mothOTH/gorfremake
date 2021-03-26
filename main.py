from turtle import Screen, Turtle
from player import Player, Missile
from enemies import BasicDude, EnemyBlock
import random
import time

screen = Screen()

screen.setup(width=640, height=480)

screen.bgcolor("black")
death = "explosion.gif"
screen.addshape(death)

FONT=("Arial", 20, "normal")
lives = 3

recorder = Turtle()
recorder.penup()
recorder.ht()
recorder.goto(-100, 0)
recorder.pencolor("White")
recorder.write("GORF Remake", font=FONT)
time.sleep(2)
recorder.clear()
recorder.goto(240, 220)
recorder.write(f"Lives: {lives}")


ship = Player()
bullet = Missile()
bullet.setheading(90)
bullet.goto(0, -200)
ship_pos = ship.xcor()
block = EnemyBlock()


game_is_on = True
invasion = []

foe_y = 235
for line in range(3):
    foe_x = -150
    foe_y -= 35
    for dude in range(6):
        foe_x += 35
        enemy = BasicDude()
        enemy.goto(foe_x, foe_y)
        enemy.showturtle()
        invasion.append(enemy)

def quit_game():
    global game_is_on
    game_is_on = False
    screen.bye()


enemy_attacks = []
laser = Missile()

for _ in range(1):
    enemy_attacks.append(laser)

enemy_step = 2
screen.tracer(2)
shot_ready = True


while game_is_on:
    screen.listen()
    screen.onkeypress(ship.move_left, "Left")
    screen.onkeypress(ship.move_right, "Right")
    screen.onkey(bullet.shoot, "Up")
    screen.onkey(quit_game, "Escape")

    ship_pos = ship.xcor()

    if bullet.ycor() > 200:
        screen.onkey(None, "Up")
        bullet.destruction()
    elif bullet.ycor() != ship.ycor():
        screen.onkey(None, "Up")
        bullet.fd(10)
    else:
        bullet.goto(ship_pos, -200)

    block_pos_x = block.xcor()
    block_pos_y = block.ycor()
    block_pos_x += enemy_step
    block.goto(block_pos_x, block_pos_y)
    if block_pos_x > 180 or block_pos_x < -180:
        enemy_step *= -1
    elif len(invasion) == 0:
        recorder.goto(-100, 0)
        recorder.write("YOU WIN!", font=FONT)
        game_is_on = False
        time.sleep(2)
        screen.bye()
    for _ in invasion:
        pos = _.xcor()
        posy = _.ycor()
        attack = random.randint(0, 100)
        if attack == 1 and shot_ready:
            laser.goto(pos, posy)
            laser.setheading(270)
            laser.shoot()
            shot_ready = False
        if abs(_.xcor() - bullet.xcor()) < 20:
            if abs(_.ycor() - bullet.ycor()) < 10:
                screen.tracer(1)
                _.shape(death)
                bullet.destruction()
                invasion.remove(_)
                _.fd(5)
                _.fd(5)
                _.ht()
                screen.tracer(2)
        if block_pos_x > 175 or block_pos_x < -175:
            posy -= 1
        pos += enemy_step
        _.goto(pos, posy)
    if not shot_ready:
        laser.fd(5)
        if abs(laser.xcor() - ship.xcor()) < 20:
            if abs(laser.ycor() - ship.ycor()) < 25:
                screen.onkeypress(None, "Left")
                screen.onkeypress(None, "Right")
                screen.onkey(None, "Up")
                screen.tracer(1)
                laser.ht()
                ship.shape(death)
                time.sleep(0.2)
                lives -= 1
                ship.new_guy(lives)
                recorder.clear()
                recorder.goto(240, 220)
                recorder.write(f"Lives: {lives}")
                if lives == 0:
                    ship.ht()
                    recorder.goto(-75, 0)
                    recorder.write("GAME OVER", font=FONT)
                    time.sleep(2)
                    game_is_on = False
                    screen.bye()
                ship.showturtle()
                screen.tracer(2)
                screen.onkeypress(ship.move_left, "Left")
                screen.onkeypress(ship.move_right, "Right")
        elif laser.ycor() < -250:
            laser.ht()
            laser.goto(320, -240)
            laser.goto(320, 240)
            shot_ready = True


screen.mainloop()
