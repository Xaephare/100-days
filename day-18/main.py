import turtle as t
import random


colors = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
          (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86),
          (73, 43, 35), (145, 178, 149), (14, 98, 70),
          (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171),
          (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
          (107, 127, 153), (176, 192, 208), (168, 99, 102)]

mans = t.Turtle()
screen = t.Screen()
screen.colormode(255)
mans.speed(0)
screen_size = screen.screensize()


def pos_bottom_left():
    mans.penup()
    mans.goto(-screen_size[0], -screen_size[1])


def next_line():
    mans.penup()
    position = mans.position()
    new_y = position[1] + 50
    mans.goto(-screen_size[0], new_y)


def draw_dots():
    mans.penup()
    for _ in range(10):
        for _ in range(10):
            mans.fd(50)
            mans.dot(20, random.choice(colors))
        next_line()


pos_bottom_left()
draw_dots()
screen.exitonclick()
