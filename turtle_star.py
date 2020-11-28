"""
Distributed under MIT License.
Copyright (c) 2020 Eui Seo Cha <zeroday0619@kakao.com> all rights reserved.
* Requires Python 3.7 or higher. but Python 3.9 not recommended
"""
import sys
import turtle
import random


class Source(turtle.Turtle):
    def __init__(self):

        turtle.bgcolor("black")
        self.screen = turtle.Screen()
        self.colors = [
            "red", "hotpink", "yellow", "skyblue"
        ]
        super().__init__()

    def n(self, a, b):
        return random.randint(a, b)

    def star(self):
        n = self.n(5, 50)
        for i in range(5):
            self.fd(n)
            self.lt(144)

    def nvlo(self, x, y):
        self.up()
        self.goto(x, y)
        no = self.n(0, 3)
        self.color(self.colors[no])
        self.down()
        self.begin_fill()
        self.star()
        self.end_fill()


app = Source()
app.screen.onclick(app.nvlo)
app.screen.listen()
try:
    app.screen.mainloop()
except KeyboardInterrupt:
    print("\nExiting")
    sys.exit(0)
