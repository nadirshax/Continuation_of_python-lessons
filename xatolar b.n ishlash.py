# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 22:23:35 2023

@author: asus
"""

import turtle

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("back")
t.pencolor("green")
a=0
b=0
t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()
while True:
    t.forword(a)
    t.right(b)
    a+=3
    b+=1
    if b ==210:
        break
    t.hideturtle()
turtle.done()
