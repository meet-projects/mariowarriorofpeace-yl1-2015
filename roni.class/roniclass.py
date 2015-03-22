import turtle
from turtle import *

screen= turtle.getscreen()
screen.register_shape("goodmario.gif")
#remember, the intersect function will use self.x, self.y but the function that check whether mario is on top of the mushroom uses bty. 

class Mario(Turtle):                                
	def __init__(self,canvas, lives, dx, dy,score,x,y, radius, bty, steps, stopfall,stopmove):
		RawTurtle.__init__(self, canvas)#good y is about -61
		self.lives= lives
		self.penup()
		self.goto(x,y)
		self.x=x
		self.y=y
		self.dx=dx
		self.dy=dy
		self.shape("goodmario.gif")
		self.score=score
		self.radius= radius
		self.stopmove=stopmove
		self.bty= bty
		self.steps=steps
		self.stopfall=stopfall
	def move_right(self): #when stating that right key calls this function remember to make the if stetement to check whether x value is between  -500<x<-250 etc.
		
		self.goto(self.x + self.dx, self.y)
		self.x= self.x +self.dx
		
	def move_left(self): 
		
		self.goto(self.x - self.dx, self.y)# remember to stop once reaches the most backish point
		self.x=self.x -self.dx
	def jump(self):
		#for a in range (1, 50):?

		self.goto(self.x, self.y + self.dy)
		self.bty=self.bty+self.dy

	def fall(self):
		self.goto(self.x, self.y-dy*2/3)
		self.bty= self.bty - dy*2/3

	
	def get_radius(self):
		return self.radius

	def distance_increase(self):
		self.steps=self.steps+1
	def distance_decrease(self):
		self.steps=self.steps-1

	def mario_dies(self):

		self.lives= self.lives-1
mario= Mario(lives=5, dx=5, dy=5, radius= 20, score=0, bty=-100, x=-400, y=-60, steps=0, canvas= screen, stopfall=False, stopmove=False)	
turtle.penup()
turtle.goto(-500,-100)
turtle.pendown()
turtle.goto(500,-100)
turtle.mainloop()
