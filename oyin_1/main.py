from turtle import Turtle , Screen
oyna = Screen()
oyna.title("birinchi oyin")
chiziq = Turtle()
chiziq.speed(0)
chiziq.color('red')
chiziq.pensize(5)
chiziq.hideturtle()
chiziq.up()
chiziq.goto(150, 150)
chiziq.down()
chiziq.goto(150, -150)
chiziq.goto(-150, -150)
chiziq.goto(-150, 150)
chiziq.goto(150, 150)
tosiq = Turtle()
tosiq.color('green')
tosiq.up()
tosiq.pensize(5)
tosiq.speed(0)
tosiq.hideturtle()
tosiq.goto(-150, -120)
tosiq.down()
tosiq.goto(-150, -150)
tosiq.goto(-50, -150)
tosiq.goto(-50, -120)
tosiq.goto(-150, -120)
koptok = Turtle()
koptok.shape('circle')
koptok.color('blue')
koptok.up()
koptok.goto(0,0)
step_x = 4
step_y = 6
while True:
    x, y = koptok.position()

    if x + step_x >= 150 or x + step_x <= -150:
        step_x = -step_x
    if y + step_y >= 150 or y + step_y <= -150:
        step_y = -step_y
    elif x + step_x <= -50  and y + step_y <= -120:
         break

    koptok.goto(x + step_x, y + step_y)

oyna.mainloop()
