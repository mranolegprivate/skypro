from turtle import *

my_turtle = Turtle()
my_turtle.speed(10)
my_turtle.screen.setup(1200, 800)

# Нарисовать квадрат
def draw_rect(t):
    for x in range(0, 4):
        t.right(180)
        t.forward(150)

# Рисует квадраты в цикле
for x in range(0, 360):
    draw_rect(my_turtle)
    my_turtle.right(1)

# Необходимо, чтобы окно не закрывалось само, а только по клику
my_turtle.screen.exitonclick()
my_turtle.screen.mainloop()