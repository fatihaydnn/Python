import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Set Up The Screen
wn = turtle.Screen()
wn.title("Sneak Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)    # Turn off the screen updates

# Sneak Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard Bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main Game Loops
while True:
    wn.update()

    # Sınırla Çarpışmayı Kontrol Et
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide The Segments
        for segment in segments:
            segment.goto(1000,1000)

        # Clear The Segments List
        segments.clear()

        # Reset The Score
        score = 0

        # Reset The Delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score),align="center",font=("Courier",24,"normal"))

    # Check For A Collision With The Food
    if head.distance(food) < 20:
        # Move The Food To A Random Spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add A Segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten The Delay
        delay -= 0.001

        # Increase(Arttırmak) Score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,high_score),align="center", font=("Courier",24,"normal"))

    # Move The End Segments First İn Reverse Order
    for index in range(len(segments) -1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x,y)

    # Move segments 0 To Where The Head İs
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # Check For Head Collision With The Body Segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide The Segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear The Segments List
            segments.clear()

            # Reset The Score
            score = 0

            # Reset The Delay
            delay = 0.1

            # Update The Score Display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score,high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()