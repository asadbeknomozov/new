# ------------------------------------------------------------------------------------------------


#           1-animation

# import turtle

# t = turtle.Turtle()
# s = turtle.Screen()

# s.bgcolor("black")
# t.speed(0)
# turtle.tracer(0)

# colors = ["#FFE0B2", "#FFB74D", "#FFA726", "#FB8C00", "#E65100"]

# while True:
#     t.clear()  # Eski chizmalarni o'chirish

#     for i in range(360):
#         t.color(colors[i % 5])
#         t.circle(140)
#         t.left(1)

#     t.right(2)  # Har safar 2° ga burilib qayta chizadi

#     turtle.update()




# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------





#               2-animation

# import turtle
# import colorsys

# t = turtle.Turtle()
# s = turtle.Screen()

# s.bgcolor("black")
# t.speed(10)
# t.width(2)

# h = 0

# for i in range(360):
#     color = colorsys.hsv_to_rgb(h, 1, 1)
#     h += 0.005

#     t.pencolor(color)

#     t.left(1)
#     t.forward(1)

#     for j in range(200):
#         t.forward(2)
#         t.left(1)

#         if 90 <= j <= 180:
#             t.right(1)

#     t.penup()
#     t.goto(0, 0)
#     t.pendown()

# turtle.done()




# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------







#           3-animation.

# import turtle
# import colorsys
# import math

# screen = turtle.Screen()
# screen.setup(800, 800)
# screen.bgcolor("black")
# screen.title("RGB Heart Animation")

# t = turtle.Turtle()
# t.speed(0)
# t.hideturtle()
# t.width(2)

# turtle.tracer(0, 0)

# h = 0

# while True:
#     t.clear()
#     t.penup()

#     h += 0.002

#     for i in range(360):
#         color = colorsys.hsv_to_rgb((h + i / 360) % 1, 1, 1)
#         t.pencolor(color)

#         angle = math.radians(i)

#         x = 16 * math.sin(angle) ** 3
#         y = (13 * math.cos(angle)
#              - 5 * math.cos(2 * angle)
#              - 2 * math.cos(3 * angle)
#              - math.cos(4 * angle))

#         x *= 18
#         y *= 18

#         t.goto(x, y)
#         t.pendown()

#     turtle.update()


# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------




#           4-animation


# import turtle
# import math
# import colorsys
# import time

# screen = turtle.Screen()
# screen.setup(900, 900)
# screen.bgcolor("black")
# screen.title("Rotating Heart Rings")
# screen.colormode(1.0)

# t = turtle.Turtle()
# t.hideturtle()
# t.speed(0)
# t.width(2)

# screen.tracer(0, 0)

# def rotate_point(x, y, deg):
#     a = math.radians(deg)
#     ca = math.cos(a)
#     sa = math.sin(a)
#     return x * ca - y * sa, x * sa + y * ca

# # Yurakning tayyor nuqtalari
# heart_points = []
# for i in range(361):
#     a = math.radians(i)
#     x = 16 * math.sin(a) ** 3
#     y = 13 * math.cos(a) - 5 * math.cos(2 * a) - 2 * math.cos(3 * a) - math.cos(4 * a)
#     heart_points.append((x, y))

# angle = 0

# while True:
#     t.clear()

#     # Ko‘p halqa
#     for ring in range(24):
#         scale = 10 + ring * 5
#         ring_angle = angle + ring * 10
#         hue = (ring / 24 + angle / 360) % 1

#         t.pencolor(colorsys.hsv_to_rgb(hue, 1, 1))
#         t.penup()

#         first = True
#         for x, y in heart_points:
#             x *= scale
#             y *= scale
#             x, y = rotate_point(x, y, ring_angle)

#             if first:
#                 t.goto(x, y)
#                 t.pendown()
#                 first = False
#             else:
#                 t.goto(x, y)

#     screen.update()
#     angle = (angle + 2) % 360
#     time.sleep(0.01)



# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------








#               5-animation

#-------------------------------------- ILON O'YINI ----------------------------------------------

# import turtle
# import time
# import random

# # Oyna sozlamalari
# screen = turtle.Screen()
# screen.title("Snake Game")
# screen.bgcolor("black")
# screen.setup(width=600, height=600)
# screen.tracer(0)

# # Ilon boshi
# head = turtle.Turtle()
# head.shape("square")
# head.color("lime")
# head.penup()
# head.goto(0, 0)
# head.direction = "stop"

# # Ovqat
# food = turtle.Turtle()
# food.shape("circle")
# food.color("red")
# food.penup()
# food.goto(random.randint(-280, 280), random.randint(-280, 280))

# # Ilon qismlari
# segments = []

# # Hisob
# score = 0
# high_score = 0

# pen = turtle.Turtle()
# pen.speed(0)
# pen.shape("circle")
# pen.color("white")
# pen.penup()
# pen.hideturtle()
# pen.goto(0, 260)
# pen.write("Score: 0  High Score: 0", align="center", font=("Arial", 18, "normal"))

# # Harakat funksiyalari
# def go_up():
#     if head.direction != "down":
#         head.direction = "up"

# def go_down():
#     if head.direction != "up":
#         head.direction = "down"

# def go_left():
#     if head.direction != "right":
#         head.direction = "left"

# def go_right():
#     if head.direction != "left":
#         head.direction = "right"

# def move():
#     if head.direction == "up":
#         y = head.ycor()
#         head.sety(y + 20)
#     elif head.direction == "down":
#         y = head.ycor()
#         head.sety(y - 20)
#     elif head.direction == "left":
#         x = head.xcor()
#         head.setx(x - 20)
#     elif head.direction == "right":
#         x = head.xcor()
#         head.setx(x + 20)

# # Tugmalar
# screen.listen()
# screen.onkeypress(go_up, "Up")
# screen.onkeypress(go_down, "Down")
# screen.onkeypress(go_left, "Left")
# screen.onkeypress(go_right, "Right")

# # Asosiy sikl
# while True:
#     screen.update()

#     # Devorga urilishi
#     if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
#         time.sleep(1)
#         head.goto(0, 0)
#         head.direction = "stop"

#         for segment in segments:
#             segment.goto(1000, 1000)

#         segments.clear()
#         score = 0
#         pen.clear()
#         pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 18, "normal"))

#     # Ovqat yeyilishi
#     if head.distance(food) < 20:
#         x = random.randint(-280, 280)
#         y = random.randint(-280, 280)
#         food.goto(x, y)

#         new_segment = turtle.Turtle()
#         new_segment.shape("square")
#         new_segment.color("green")
#         new_segment.penup()
#         segments.append(new_segment)

#         score += 10
#         if score > high_score:
#             high_score = score

#         pen.clear()
#         pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 18, "normal"))

#     # Ilon qismlarini orqaga qarab yuritish
#     for index in range(len(segments) - 1, 0, -1):
#         x = segments[index - 1].xcor()
#         y = segments[index - 1].ycor()
#         segments[index].goto(x, y)

#     # Birinchi qism boshga ergashadi
#     if len(segments) > 0:
#         x = head.xcor()
#         y = head.ycor()
#         segments[0].goto(x, y)

#     move()

#     # O'ziga urilishi
#     for segment in segments:
#         if segment.distance(head) < 20:
#             time.sleep(1)
#             head.goto(0, 0)
#             head.direction = "stop"

#             for s in segments:
#                 s.goto(1000, 1000)

#             segments.clear()
#             score = 0
#             pen.clear()
#             pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 18, "normal"))

#     time.sleep(0.1)

# turtle.done()



# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------



#               6-animation.


# import turtle
# import math

# screen = turtle.Screen()
# screen.bgcolor("black")
# screen.title("Heart Animation")

# t = turtle.Turtle()
# t.speed(0)
# t.hideturtle()
# t.width(2)

# colors = [
#     "#ff0000",
#     "#ff1493",
#     "#ff4500",
#     "#ff69b4",
#     "#ff6347",
#     "#ff00ff"
# ]

# scale = 12
# grow = 0.15

# while True:
#     for color in colors:
#         t.clear()
#         t.color(color)
#         t.penup()

#         first = True

#         for i in range(361):
#             a = math.radians(i)

#             x = 16 * math.sin(a) ** 3
#             y = (13 * math.cos(a)
#                  - 5 * math.cos(2 * a)
#                  - 2 * math.cos(3 * a)
#                  - math.cos(4 * a))

#             x *= scale
#             y *= scale

#             if first:
#                 t.goto(x, y)
#                 t.pendown()
#                 first = False
#             else:
#                 t.goto(x, y)

#         scale += grow

#         if scale > 15:
#             grow = -0.15
#         elif scale < 11:
#             grow = 0.15

#         screen.update()





#               7-animation.

# from typing import List

# from PIL.Image import Image

# from animeface import _nvxs


# class Point:
#     x: int
#     y: int

#     def __init__(self, x: int, y: int):
#         self.x, self.y = x, y

#     def __repr__(self):
#         return '(%d, %d)' % (self.x, self.y)


# class Box:
#     x: int
#     y: int
#     width: int
#     height: int

#     def __init__(self, x: int, y: int, width: int, height: int):
#         self.x, self.y = x, y
#         self.width, self.height = width, height

#     def __repr__(self):
#         return '(%d, %d; %d, %d)' % (self.x, self.y, self.width, self.height)


# class Color:
#     r: int
#     g: int
#     b: int

#     def __init__(self, r: int, g: int, b: int):
#         self.r, self.g, self.b = r, g, b

#     def __repr__(self):
#         return '(%d, %d, %d)' % (self.r, self.g, self.b)


# class BoxColorPart:
#     pos: Box
#     color: Color

#     def __init__(self, pos: Box, color: Color):
#         self.pos = pos
#         self.color = color

#     def __repr__(self):
#         return '<pos=%r, color=%r>' % (self.pos, self.color)


# class PointPart:
#     pos: Point

#     def __init__(self, pos: Point):
#         self.pos = pos

#     def __repr__(self):
#         return '<pos=%r>' % (self.pos, )


# class BoxPart:
#     pos: Box

#     def __init__(self, pos: Box):
#         self.pos = pos

#     def __repr__(self):
#         return '<pos=%r>' % (self.pos, )


# class ColorPart:
#     color: Color

#     def __init__(self, color: Color):
#         self.color = color

#     def __repr__(self):
#         return '<color=%r>' % (self.color, )


# class Face:
#     likelihood: float
#     face: BoxPart
#     skin: ColorPart
#     hair: ColorPart
#     left_eye: BoxColorPart
#     right_eye: BoxColorPart
#     mouth: BoxPart
#     nose: PointPart
#     chin: PointPart

#     def __init__(self, result):
#         self.likelihood = result['likelihood']
#         self.face = BoxPart(Box(*result['face_box']))
#         self.skin = ColorPart(Color(*result['skin_color']))
#         self.hair = ColorPart(Color(*result['hair_color']))
#         self.left_eye = BoxColorPart(Box(*result['left_eye_box']),
#                                      Color(*result['left_eye_color']))
#         self.right_eye = BoxColorPart(Box(*result['right_eye_box']),
#                                       Color(*result['right_eye_color']))
#         self.mouth = BoxPart(Box(*result['mouth_box']))
#         self.nose = PointPart(Point(*result['nose_point']))
#         self.chin = PointPart(Point(*result['chin_point']))

#     def __repr__(self):
#         return ('<animeface.Face '
#                 'likelihood=%(likelihood)f '
#                 'face=%(face)r '
#                 'skin=%(skin)r '
#                 'hair=%(hair)r '
#                 'left_eye=%(left_eye)r '
#                 'right_eye=%(right_eye)r '
#                 'mouth=%(mouth)r '
#                 'nose=%(nose)r '
#                 'chin=%(chin)r>') % self.__dict__


# def detect(im: Image) -> List[Face]:
#     """Detects anime faces.

#   Args:
#     im: PIL.Image object.

#   Returns:
#     A list of Face.
#   """
#     if im.mode in ('RGB', 'L'):
#         pass  # Fine.
#     elif im.mode == '1':
#         im = im.convert('L')
#     elif im.mode in ('P', 'RGBA', 'CMYK', 'YCbCr'):
#         im = im.convert('RGB')
#     else:
#         raise ValueError('Unsupported color mode: %s' % im.mode)
#     results = _nvxs.detect(im.getdata())
#     return [Face(result) for result in results]





#               8-animation.

# import turtle
# import colorsys
# import math


# def draw_vortex_effect():
#     screen = turtle.Screen()
#     screen.bgcolor("black")
#     screen.title("Chromospheric Vortex")

#     t = turtle.Turtle()
#     t.speed(0)
#     t.hideturtle()

#     screen.tracer(2, 0)

#     hue = 0.0
#     iterations = 400
#     magic_angle = 121

#     try:
#         for i in range(iterations):
#             # Rainbow color effect
#             color = colorsys.hsv_to_rgb(hue, 0.9, 1)
#             t.pencolor(color)
#             hue += 1 / iterations

#             # Dynamic pen width
#             width = (math.sin(i * 0.05) * 2) + 3
#             t.width(width)

#             # Main drawing
#             t.forward(i * 1.5)
#             t.left(magic_angle)
#             t.circle(i, 90)
#             t.right(45)

#             t.forward(i * 1.5)
#             t.left(magic_angle)
#             t.circle(i, 90)
#             t.right(45)

#             screen.update()

#     except turtle.Terminator:
#         print("Window closed.")


# draw_vortex_effect()
# turtle.done()




#               9-animation.

# import turtle
# import math
# import colorsys
# import random

# screen = turtle.Screen()
# screen.bgcolor("black")
# screen.title("❤️ I LOVE YOU ❤️")
# screen.setup(900, 900)

# screen.tracer(0)

# # Yulduzlar
# stars = turtle.Turtle()
# stars.hideturtle()
# stars.speed(0)
# stars.penup()

# for _ in range(250):
#     stars.goto(random.randint(-450, 450), random.randint(-450, 450))
#     stars.dot(random.randint(1, 3), "white")

# t = turtle.Turtle()
# t.speed(0)
# t.hideturtle()
# t.penup()

# scale = 13
# direction = 0.15
# hue = 0

# while True:

#     t.clear()

#     hue += 0.003
#     if hue > 1:
#         hue = 0

#     rgb = colorsys.hsv_to_rgb(hue, 1, 1)
#     t.color(rgb)

#     scale += direction

#     if scale > 17:
#         direction = -0.15

#     if scale < 13:
#         direction = 0.15

#     for i in range(180):

#         angle = math.radians(i * 2)

#         x = 16 * (math.sin(angle) ** 3) * scale

#         y = (13 * math.cos(angle)
#              - 5 * math.cos(2 * angle)
#              - 2 * math.cos(3 * angle)
#              - math.cos(4 * angle)) * scale

#         t.goto(x, y)

#         size = int(8 + 3 * abs(math.sin(angle * 4)))

#         t.write(
#             "I LOVE YOU",
#             align="center",
#             font=("Arial", size, "bold")
#         )

#     # Markazdagi yozuv
#     t.goto(0, -20)
#     t.color("white")
#     t.write(
#         "❤️ FOREVER ❤️",
#         align="center",
#         font=("Arial", 26, "bold")
#     )

#     screen.update()

# turtle.done()


















































