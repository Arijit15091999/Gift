# main.py

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
import turtle

import turtle as tur

class DrawingScreen(Screen):
    def on_enter(self):
        # import drawing
        my_drawing()

class DrawingApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(DrawingScreen(name='drawing'))
        return sm

def my_drawing():
    tur.title("For Sonali")

    tur.write("Specially for Sonali !                    ", align="right", )

    # Set initial position

    turtle.penup()

    turtle.left(90)

    turtle.fd(200)

    turtle.pendown()

    turtle.right(90)

    # flower base

    turtle.fillcolor("red")

    turtle.begin_fill()

    turtle.circle(10, 180)

    turtle.circle(25, 110)

    turtle.left(50)

    turtle.circle(60, 45)

    turtle.circle(20, 170)

    turtle.right(24)

    turtle.fd(30)

    turtle.left(10)

    turtle.circle(30, 110)

    turtle.fd(20)

    turtle.left(40)

    turtle.circle(90, 70)

    turtle.circle(30, 150)

    turtle.right(30)

    turtle.fd(15)

    turtle.circle(80, 90)

    turtle.left(15)

    turtle.fd(45)

    turtle.right(165)

    turtle.fd(20)

    turtle.left(155)

    turtle.circle(150, 80)

    turtle.left(50)

    turtle.circle(150, 90)

    turtle.end_fill()

    # Petal 1

    turtle.left(150)

    turtle.circle(-90, 70)

    turtle.left(20)

    turtle.circle(75, 105)

    turtle.setheading(60)

    turtle.circle(80, 98)

    turtle.circle(-90, 40)

    # Petal 2

    turtle.left(180)

    turtle.circle(90, 40)

    turtle.circle(-80, 98)

    turtle.setheading(-83)

    # Leaves 1

    turtle.fd(30)

    turtle.left(90)

    turtle.fd(25)

    turtle.left(45)

    turtle.fillcolor("green")

    turtle.begin_fill()

    turtle.circle(-80, 90)

    turtle.right(90)

    turtle.circle(-80, 90)

    turtle.end_fill()

    turtle.right(135)

    turtle.fd(60)

    turtle.left(180)

    turtle.fd(85)

    turtle.left(90)

    turtle.fd(80)

    # Leaves 2

    turtle.right(90)

    turtle.right(45)

    turtle.fillcolor("green")

    turtle.begin_fill()

    turtle.circle(80, 90)

    turtle.left(90)

    turtle.circle(80, 90)

    turtle.end_fill()

    turtle.left(135)

    turtle.fd(60)

    turtle.left(180)

    turtle.fd(60)

    turtle.right(90)

    turtle.circle(226, 60)

    # heart

    turtle.pensize(4)

    turtle.color("red")

    turtle.left(50)

    turtle.forward(200)

    turtle.circle(70, 200)

    turtle.right(140)

    turtle.circle(70, 200)

    turtle.forward(200)

    turtle.done()



if __name__ == '__main__':
    DrawingApp().run()
