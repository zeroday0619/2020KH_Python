"""
Distributed under MIT License.
Copyright (c) 2020 Eui Seo Cha <zeroday0619@kakao.com> all rights reserved.
* Requires Python 3.7 or higher. but Python 3.9 not recommended
"""
import os
import sys
import random
import turtle


class CarRacing:
    def __init__(self):
        self.path = os.path.dirname(__file__)
        self.img1 = self.path+"/car.gif"
        self.img2 = self.path+"/car2.gif"
        print(self.img1)
        self.screen = turtle.Screen()

    def Player(self, no: int, img_name: str):
        t = turtle.Turtle()
        t.shape(img_name)
        t.pensize(3)
        t.penup()
        t.goto(-self.screen.canvwidth, -200*(no - 1))
        return t

    def n(self, a, b):
        return random.randint(a, b)

    def start(self):
        self.screen.addshape(app.img1)
        self.screen.addshape(app.img2)
        A = self.Player(1, app.img1)
        B = self.Player(2, app.img2)

        A.pendown()
        B.pendown()
        A.speed(0)
        B.speed(0)

        for i in range(50):
            AX = self.n(1, 60)
            AY = self.n(1, 60)
            A.fd(AX)
            B.fd(AY)

            if A.pos()[0] > self.screen.canvwidth or B.pos()[0] > self.screen.canvwidth:
                if A.pos()[0] > B.pos()[0]:
                    print("1번 승리")
                else:
                    print("2번 승리")
                break
        print("레이싱 종료")


try:
    app = CarRacing()
    app.start()
    app.screen.mainloop()
except KeyboardInterrupt:
    sys.exit(0)
