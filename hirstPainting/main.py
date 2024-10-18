# import colorgram
# colors = colorgram.extract('image.png', 30)
# rgb_colors = []
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     new_color = (red, green, blue)
#     rgb_colors.append(new_color)
# print(rgb_colors)
from turtle import Screen
import turtle as turtle_module
import random

color_list = [(199, 159, 94), (63, 88, 126), (138, 90, 51), (218, 205, 122), (134, 170, 193), (145, 54, 83), (123, 36, 48), (47, 54, 101), (139, 184, 144), (77, 26, 45), (174, 100, 110), (41, 42, 60), (149, 172, 67), (179, 143, 171), (57, 40, 32), (94, 126, 178), (182, 87, 78), (104, 155, 97), (72, 114, 112), (169, 205, 154), (78, 73, 47), (212, 179, 188), (50, 70, 73), (180, 189, 209), (214, 182, 174), (130, 44, 43)]

tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.speed("fastest")
tim.penup()
tim.shape("turtle")

# move turtle to up left corner
tim.setheading(135)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    # pick a random color for tim
    random_color = random.choice(color_list)
    tim.color(random_color)
    tim.dot(25, random_color)
    tim.forward(50)

    # change direction after 10 dots
    if dot_count % 10 == 0:
        # move turtle to the left and down 1 step
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(270)
        tim.forward(50)
        tim.setheading(0)

tim.hideturtle()
Screen().exitonclick()