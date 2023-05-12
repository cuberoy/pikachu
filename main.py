# Author: cuberoy
# Created: 11 Nov 2022, 7pm
# Email: roytan2911@gmail.com

"""----------------------------------------------------------------------------
MIT License

Copyright (c) 2022 cuberoy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/o sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
----------------------------------------------------------------------------"""

import turtle

# Setup turtle
t = turtle.Turtle()
t.shape('blank')
t.speed(0)
t.screen.setworldcoordinates(-5000, -5000, 5000, 5000)
t.screen.title('PIKACHU')
t.screen.colormode(255)

def paint_background(i, y_pos):
    t.penup()
    if i % 2 == 0:
        t.goto(-5000, y_pos)
        t.setheading(0)
    else:
        t.goto(5000, y_pos)
        t.setheading(180)
    t.pendown()
    t.fd(10000)
    return

def draw_background():
    t.pensize(8)
    background_y_pos = 5000
    # ----------------------------------------------------------------------------
    # RGB gradient color for the sky
    # (105, 0, 0) -> (255, 93, 0) -> (255, 200, 0)
    # Sky
    for i in range(50):
        r = 105 + 150 * i // 50
        g = 0 + 93 * i // 50
        b = 0
        col = (r, g, b)
        t.color(col)
        paint_background(i, background_y_pos)
        background_y_pos = background_y_pos - 75
    for i in range(50):
        r = 255
        g = 93 + 107 * i // 50
        b = 0
        col = (r, g, b)
        t.color(col)
        paint_background(i, background_y_pos)
        background_y_pos = background_y_pos - 75
    # ----------------------------------------------------------------------------
    # RGB gradient color for the grass
    # (0, 93, 0) -> (0, 200, 0)
    # Grass
    for i in range(50):
        r = 0
        g = 93 + 107 * i // 50
        b = 0
        col = (r, g, b)
        t.color(col)
        paint_background(i, background_y_pos)
        background_y_pos = background_y_pos - 50
    # ----------------------------------------------------------------------------
    # Cloud 1
    FRONT_CLOUD = (199, 196, 191)
    BACK_CLOUD = (169, 169, 169)
    t.setheading(0)
    t.penup()
    t.pensize(6)
    t.goto(-4800, 4300)
    t.dot(20, BACK_CLOUD)
    t.goto(-4400, 4150)
    t.dot(25, BACK_CLOUD)
    t.goto(-5000, 4100)
    t.begin_fill()
    t.color(FRONT_CLOUD)
    t.circle(150, 180)
    t.end_fill()
    t.goto(-5000, 4150)
    t.setheading(90)
    t.pendown()
    t.forward(210)
    t.penup()
    t.goto(-4700, 4125)
    t.dot(30, FRONT_CLOUD)
    t.goto(-4500, 4400)
    t.dot(32.5, FRONT_CLOUD)
    t.goto(-4150, 4400)
    t.dot(27.5, FRONT_CLOUD)
    # ----------------------------------------------------------------------------
    # Cloud 2
    t.goto(-2000, 4550)
    t.dot(23, BACK_CLOUD)
    t.goto(-1550, 4850)
    t.dot(15, BACK_CLOUD)
    t.goto(-1850, 4750)
    t.dot(27.5, FRONT_CLOUD)
    t.goto(-1780, 4450)
    t.dot(15, FRONT_CLOUD)
    t.goto(-1600, 4650)
    t.dot(19, FRONT_CLOUD)
    t.goto(-1500, 4650)
    t.dot(19, FRONT_CLOUD)
    # ----------------------------------------------------------------------------
    # Cloud 3
    t.goto(1700, 4300)
    t.dot(15, BACK_CLOUD)
    t.goto(1950, 4650)
    t.dot(25, BACK_CLOUD)
    t.goto(2200, 4560)
    t.dot(20, BACK_CLOUD)
    t.goto(2080, 4500)
    t.dot(24, FRONT_CLOUD)
    t.goto(1850, 4500)
    t.dot(21, FRONT_CLOUD)
    t.goto(1750, 4600)
    t.dot(21, FRONT_CLOUD)
    t.goto(1900, 4150)
    t.dot(30, FRONT_CLOUD)
    t.goto(2080, 4380)
    t.dot(22, FRONT_CLOUD)
    t.goto(2200, 4380)
    t.dot(22, FRONT_CLOUD)
    t.goto(2320, 4380)
    t.dot(22, FRONT_CLOUD)
    # ----------------------------------------------------------------------------
    # Sun
    t.goto(4000, 4000)
    t.dot(100, (250, 220, 88))

def draw_pikachu():
    t.pensize(3)
    t.color("black")
    # ----------------------------------------------------------------------------
    # Tail
    t.fillcolor(240, 210, 38)
    t.penup()
    t.goto(-1895, -1940)
    t.begin_fill()
    t.pendown()
    t.setheading(145)
    t.fd(600)
    t.setheading(68)
    t.fd(1150)
    t.setheading(140)
    t.fd(1200)
    t.setheading(65)
    t.fd(1900)
    t.goto(-2920, 2650)
    t.setheading(85)
    t.fd(2100)
    t.setheading(320)
    t.fd(2950)
    t.setheading(240)
    t.fd(260)
    t.end_fill()
    # ----------------------------------------------------------------------------
    # Right leg
    t.fillcolor(250, 230, 45)
    t.penup()
    t.goto(1850, -3080)
    t.pendown()
    t.begin_fill()
    t.setheading(315)
    for i in range(7):
        t.fd(100)
        t.right(6)
    t.penup()
    t.goto(2000, -3960)
    t.pendown()
    t.setheading(50)
    t.fd(730)
    for i in range(36):
        t.fd(7)
        t.right(5)
    toe_one = t.pos()
    t.fd(790)
    t.penup()
    t.goto(toe_one)
    t.pendown()
    t.setheading(50)
    t.fd(50)
    for i in range(36):
        t.fd(7)
        t.right(5)
    toe_two = t.pos()
    t.fd(890)
    t.penup()
    t.goto(toe_two)
    t.pendown()
    t.setheading(50)
    t.bk(100)
    for i in range(36):
        t.fd(7)
        t.right(5)
    t.left(4)
    for i in range(13):
        t.fd(90)
        t.right(1)
    t.left(1)
    for i in range(12):
        t.fd(20 + i * 4)
        t.right(7 + i)
    t.left(10)
    t.fd(80)
    t.penup()
    t.goto(1670, -4505)
    t.pendown()
    t.setheading(186)
    for i in range(5):
        t.fd(40)
        t.right(1)
    t.end_fill()
    # ----------------------------------------------------------------------------
    # Left leg
    t.penup()
    t.goto(-1940, -3070)
    t.pendown()
    t.begin_fill()
    t.setheading(225)
    for i in range(7):
        t.fd(100)
        t.left(6)
    t.penup()
    t.goto(-2090, -3930)
    t.pendown()
    t.setheading(130)
    t.fd(730)
    for i in range(36):
        t.fd(7)
        t.left(5)
    toe_one = t.pos()
    t.fd(790)
    t.penup()
    t.goto(toe_one)
    t.pendown()
    t.setheading(130)
    t.fd(50)
    for i in range(36):
        t.fd(7)
        t.left(5)
    toe_two = t.pos()
    t.fd(890)
    t.penup()
    t.goto(toe_two)
    t.pendown()
    t.setheading(130)
    t.bk(100)
    for i in range(36):
        t.fd(7)
        t.left(5)
    t.right(4)
    for i in range(13):
        t.fd(90)
        t.left(1)
    t.right(1)
    for i in range(12):
        t.fd(20 + i * 4)
        t.left(7 + i)
    t.fd(80)
    t.penup()
    t.goto(-1770, -4505)
    t.pendown()
    t.setheading(6)
    for i in range(5):
        t.fd(40)
        t.right(1)
    t.end_fill()
    # ----------------------------------------------------------------------------
    # Butt
    t.penup()
    t.goto(-640, -4500)
    t.pendown()
    t.setheading(5)
    t.begin_fill()
    for i in range(4):
        t.fd(300)
        t.right(4)
    # ----------------------------------------------------------------------------
    # Right hand
    t.penup()
    t.goto(800, -2500)
    t.pendown()
    t.setheading(250)
    for i in range(30):
        t.fd(70)
        t.left(1)
    t.left(20)
    t.fd(90)
    t.penup()
    t.goto(700, -4480)
    t.pendown()
    t.setheading(270)
    t.fd(250)
    t.setheading(60)
    t.fd(200)
    t.setheading(280)
    t.fd(210)
    t.setheading(60)
    t.fd(210)
    t.setheading(282.5)
    t.fd(210)
    t.setheading(62.5)
    t.fd(210)
    t.setheading(285)
    t.fd(210)
    t.setheading(65)
    t.fd(210)
    t.setheading(287.5)
    t.fd(210)
    t.setheading(67.5)
    t.fd(105)
    t.setheading(60)
    for i in range(50):
        t.fd(70)
        t.left(1)
    t.fd(200)
    # ----------------------------------------------------------------------------
    # Right face
    t.penup()
    t.goto(1010, -1800)
    t.pendown()
    t.setheading(40)
    for i in range(13):
        t.fd(70)
        t.left(2)
    t.setheading(70)
    for i in range(8):
        t.fd(70)
        t.left(1)
    for i in range(11):
        t.fd(70)
        t.left(3)
    t.setheading(75)
    for i in range(8):
        t.fd(100)
        t.left(2)
    for i in range(15):
        t.fd(70)
        t.left(2)
    # ----------------------------------------------------------------------------
    # Right ear
    t.penup()
    t.goto(1610, 1830)
    t.pendown()
    t.setheading(65)
    for i in range(7):
        t.fd(200)
        t.left(2)
    for i in range(6):
        t.fd(270)
        t.left(4)
    t.setheading(230)
    for i in range(6):
        t.fd(270)
        t.left(4)
    for i in range(9):
        t.fd(100)
        t.left(1)
    # ----------------------------------------------------------------------------
    # Head
    t.penup()
    t.goto(1150, 2400)
    t.pendown()
    t.setheading(150)
    for i in range(16):
        t.fd(150)
        t.left(4)
    # ----------------------------------------------------------------------------
    # Left ear
    t.penup()
    t.goto(-1101.57, 2486.32)
    t.pendown()
    t.setheading(135)
    for i in range(9):
        t.fd(100)
        t.left(1)
    for i in range(6):
        t.fd(270)
        t.left(4)
    t.setheading(295)
    for i in range(6):
        t.fd(270)
        t.left(4)
    for i in range(9):
        t.fd(100)
        t.left(1)
    # ----------------------------------------------------------------------------
    # Left face
    t.penup()
    t.goto(-1526.96, 1998.36)
    t.pendown()
    t.setheading(239)
    for i in range(15):
        t.fd(70)
        t.left(2)
    for i in range(8):
        t.fd(100)
        t.left(2)
    t.setheading(249)
    for i in range(11):
        t.fd(70)
        t.left(3)
    for i in range(8):
        t.fd(70)
        t.left(1)
    t.setheading(294)
    for i in range(13):
        t.fd(70)
        t.left(2)
    # ----------------------------------------------------------------------------
    # Left hand
    t.penup()
    t.goto(-1630, -1140)
    t.pendown()
    t.setheading(250)
    t.fd(200)
    for i in range(50):
        t.fd(70)
        t.left(1)
    t.setheading(291.5)
    t.fd(105)
    t.setheading(72.5)
    t.fd(210)
    t.setheading(295)
    t.fd(210)
    t.setheading(75)
    t.fd(210)
    t.setheading(297.5)
    t.fd(210)
    t.setheading(77.5)
    t.fd(210)
    t.setheading(300)
    t.fd(210)
    t.setheading(80)
    t.fd(210)
    t.setheading(302.5)
    t.fd(200)
    t.setheading(90)
    t.fd(250)
    t.penup()
    t.goto(-750, -4644.5)
    t.pendown()
    t.setheading(60)
    t.fd(90)
    t.left(20)
    for i in range(30):
        t.fd(70)
        t.left(1)
    t.end_fill()
    # ----------------------------------------------------------------------------
    # Right ear black
    t.penup()
    t.goto(2064.69, 3150.5)
    t.pendown()
    t.setheading(79)
    t.fillcolor("black")
    t.begin_fill()
    for i in range(6):
        t.fd(270)
        t.left(4)
    t.setheading(230)
    for i in range(6):
        t.fd(135)
        t.left(2)
    t.end_fill()
    # ----------------------------------------------------------------------------
    # Left ear black
    t.penup()
    t.goto(-2303.23, 2463.68)
    t.pendown()
    t.setheading(139)
    t.begin_fill()
    for i in range(6):
        t.right(4)
        t.fd(270)
    t.setheading(346)
    for i in range(6):
        t.right(2)
        t.fd(135)
    t.end_fill()
    # ----------------------------------------------------------------------------
    # Brown eyes
    t.color(89, 50, 27)
    t.penup()
    t.goto(-900, 725)
    t.dot(40)
    t.goto(900, 725)
    t.dot(40)
    # ----------------------------------------------------------------------------
    # Black eyes
    t.color("black")
    t.goto(-875, 750)
    t.dot(32)
    t.goto(875, 750)
    t.dot(32)
    # ----------------------------------------------------------------------------
    # White eyes
    t.color("white")
    t.goto(-800, 825)
    t.dot(15)
    t.goto(800, 825)
    t.dot(15)
    t.goto(-1050, 675)
    t.dot(7)
    t.goto(1050, 675)
    t.dot(7)
    # ----------------------------------------------------------------------------
    # Nose
    t.color("black")
    t.setheading(270)
    t.goto(0, 350)
    t.shape("circle")
    t.shapesize(0.06, 0.35, 2)
    t.stamp()
    t.shape("blank")
    # ----------------------------------------------------------------------------
    # Lower Mouth
    t.penup()
    t.goto(-295, -264.98)
    t.pendown()
    t.fillcolor(240, 84, 97)
    t.begin_fill()
    t.setheading(273)
    for i in range(10):
        t.fd(50)
        t.left(1)
    for i in range(30):
        t.fd(12)
        t.left(2)
    t.setheading(17)
    for i in range(30):
        t.left(2)
        t.fd(12)
    for i in range(10):
        t.left(1)
        t.fd(50)
    # ----------------------------------------------------------------------------
    # Tongue
    t.penup()
    t.goto(245, -450)
    t.pendown()
    t.setheading(134)
    for i in range(10):
        t.fd(55)
        t.left(10)
    t.end_fill()
    # ----------------------------------------------------------------------------
    # Upper Mouth
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.setheading(250)
    t.fillcolor(112, 8, 5)
    t.begin_fill()
    for i in range(10):
        t.fd(55)
        t.right(11)
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.setheading(290)
    for i in range(10):
        t.fd(55)
        t.left(11)
    t.penup()
    t.goto(295, -264.98)
    t.pendown()
    t.setheading(267)
    for i in range(2):
        t.fd(50)
        t.right(1)
    t.penup()
    t.goto(245, -450)
    t.pendown()
    t.setheading(134)
    for i in range(10):
        t.fd(55)
        t.left(10)
    t.penup()
    t.goto(-295, -264.98)
    t.pendown()
    t.setheading(273)
    for i in range(2):
        t.fd(50)
        t.left(1)
    t.end_fill()
    t.color(112, 8, 5)
    t.penup()
    t.goto(-250, -300)
    t.dot(4)
    t.goto(-250, -400)
    t.dot(4)
    t.goto(250, -400)
    t.dot(4)
    t.color("black")
    t.fillcolor(250, 230, 45)
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.setheading(250)
    t.begin_fill()
    for i in range(10):
        t.fd(55)
        t.right(11)
    t.end_fill()
    # ----------------------------------------------------------------------------
    # Left cheek
    t.penup()
    t.goto(-1800, -60)
    t.pendown()
    t.fillcolor(233, 41, 41)
    t.begin_fill()
    t.setheading(5)
    for i in range(19):
        t.fd(75)
        t.right(10)
    t.penup()
    t.goto(-1732.44, -879.67)
    t.pendown()
    t.setheading(109)
    for i in range(4):
        t.right(1)
        t.fd(70)
    for i in range(8):
        t.right(3)
        t.fd(70)
    t.end_fill()
    # ----------------------------------------------------------------------------
    # Right cheek
    t.penup()
    t.goto(1710, -60)
    t.pendown()
    t.begin_fill()
    t.setheading(175)
    for i in range(19):
        t.fd(75)
        t.left(10)
    t.penup()
    t.goto(1633.85, -890.47)
    t.pendown()
    t.setheading(73)
    for i in range(6):
        t.fd(70)
        t.left(1)
    for i in range(5):
        t.fd(70)
        t.left(3)
    t.end_fill()

draw_background()
draw_pikachu()
turtle.done()