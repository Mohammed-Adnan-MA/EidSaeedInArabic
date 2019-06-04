import turtle
from random import randint
#The line below is imported for the sake of half moon's random colors
#import random

def drawing_shapes():

	#turtle.setup( width = 500, height = 500, startx = None, starty = None)
	window = turtle.Screen()
	window.bgcolor("Black")
	window.title("Eid Saeed")

	#Draw half a moon using circles:
	halfMoon= turtle.Turtle()
	halfMoon.color("White")
	halfMoon.shape("circle")
	halfMoon.speed(1)
	spaceBetweenCircles = 5

	halfMoon.up()
	halfMoon.setposition(500,380)
	halfMoon.down()

	halfMoon.speed(16)
	for i in range(35):
		halfMoon.left(5.5)
		halfMoon.up()
		if spaceBetweenCircles < 30:
			halfMoon.forward(-15)
		else:
			halfMoon.forward(-30)	
		halfMoon.down()
		#random colors for the half moon
		#R = random.random()
   		#G = random.random()
   		#B = random.random()
		#halfMoon.color((R, G, B))
		halfMoon.begin_fill()
		for count in range(4):
			halfMoon.circle(spaceBetweenCircles, -180)
			if i < 18:
				spaceBetweenCircles += 1
			else:
				spaceBetweenCircles -=1	
		halfMoon.end_fill()
	halfMoon.hideturtle()


	#id Saeed in Arabic:
	eid=turtle.Turtle()
	eid.shape("arrow")
	eid.color("White")
	eid.speed(4)
	eid.pensize(20)

	eid.up()
	eid.setposition(580,-321)
	eid.down()

	#Eid	
	eid.left(180)	
	eid.forward(350)
	eid.right(90)
	eid.forward(100)
	eid.left(180)
	eid.forward(100)
	eid.right(90)
	eid.forward(120)
	eid.right(80)
	eid.forward(100)
	eid.left(180)
	eid.forward(100)
	eid.right(100)
	eid.forward(100)
	eid.up()
	eid.setposition(220,-365)
	eid.down()
	eid.begin_fill()
	for _ in range(5):
		eid.pensize(3)
		eid.forward(30)
		eid.right(146)
	eid.end_fill()

	eid.up()
	eid.setposition(175,-365)
	eid.down()
	eid.begin_fill()
	for _ in range(5):
		eid.forward(30)
		eid.right(146)
	eid.end_fill()

	#Saeed
	eid.pensize(20)
	eid.up()
	eid.setposition(-50,-220)
	eid.down()
	eid.left(110)
	eid.forward(100)
	eid.right(90)
	eid.forward(93)
	eid.right(90)
	eid.forward(100)
	eid.left(180)
	eid.forward(100)
	eid.right(90)
	eid.forward(93)
	eid.right(90)
	eid.forward(100)
	eid.left(180)
	eid.forward(100)
	eid.right(90)
	eid.forward(120)
	for _ in range(4):
		eid.forward(100)
		eid.right(90)
	eid.forward(140)
	eid.right(90)
	eid.forward(100)
	eid.left(180)
	eid.forward(100)
	eid.right(90)
	eid.forward(120)
	eid.right(80)
	eid.forward(100)
	eid.left(180)
	eid.forward(100)
	eid.right(100)
	eid.forward(100)
	eid.up()
	eid.setposition(-500,-365)
	eid.down()
	eid.pensize(3)
	eid.begin_fill()
	for _ in range(5):
		eid.forward(30)
		eid.right(146)
	eid.end_fill()

	eid.up()
	eid.setposition(-540,-365)
	eid.down()
	eid.begin_fill()
	for _ in range(5):
		eid.forward(30)
		eid.right(146)
	eid.end_fill()


	eid.up()
	eid.setposition(-538,-635)
	eid.down()	


	#Sky Stars in random positions
	star= turtle.Turtle()
	star.color("White")
	star.shape("arrow")
	star.speed(0)
	star.fillcolor("White")

	xCoordinate=0
	yCoordinate=0
	for i in range(300):
		xCoordinate=randint(-900,900)
		xCoordinate+=5
		yCoordinate=randint(-200,380)
		yCoordinate+=5
		star.up()
		star.setposition(xCoordinate,yCoordinate)
		star.down()
		star.begin_fill()
		for count in range(5):
			star.forward(20)
			star.right(146)
		star.end_fill()	
	star.hideturtle()
	
	window.exitonclick()
drawing_shapes()
