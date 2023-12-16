import turtle

# turtle - rysunki generowan za pomocą zółwia

t = turtle.Turtle()
t.speed(100)
t.setheading(90)  # ustawienie głowy zółwia 90 stopni
t.penup()  # podniesienie długopisu
t.goto(0, -200)  # x, y
t.pendown()  # opuszczenie długopisu


def branch(t, len):
    if len == 0: return
    nt = t.clone()
    nt.forward(50)
    nt.left(20)
    branch(nt, len - 1)
    nt.right(40)
    nt.forward(20)
    branch(nt, len - 1)


branch(t, 7)
window = turtle.Screen()
window.mainloop()  # wystartowanie okna
# window.exitonclick()