import turtle
from turtle import *
import random
screen= turtle.getscreen()
screen.register_shape("goodmushrooms.gif")

class Good_mushrooms(Turtle):
	def __init__(self,canvas,x,y,dx,radius):
		RawTurtle.__init__(self,canvas)
		self.penup()
		self.goto(x,y)
		self.dx = dx
		self.radius=radius
		self.shape("goodmushrooms.gif")
		 

	def getDX(self):
		return self.dx
    
	def setDX(self,dx):
		self.dx = dx
    
	def moveleft(self):
		x = self.xcor()
		self.goto(x-dx,y)
    
	def getRadius(self):
		return self.radius
	def die(self):
		self.hide()

class Holes(Turtle):
	def __init__(self,canvas,dx,x,y,size):
		RawTurtle.__init__(self,canvas)
		self.penup()
		self.color("lightblue")
		self.size = size
		self.goto(x,y)
		self.dx = dx
		self.shape("hole"+ str(size))
 
	def getDX(self):
		return self.dx
    
	def setDX(self,dx):
		self.dx =dx                                                  
    
	def moveleft(self):
		dx=-1

screen.register_shape("hole1",((250,-500),(250,-400),(150,-400),(150,-500)))
screen.register_shape("hole2",((250,-500),(250,-400),(100,-400),(100,-500)))
screen.register_shape("hole3",((250,-500),(250,-400),(200,-400),(200,-500)))



 