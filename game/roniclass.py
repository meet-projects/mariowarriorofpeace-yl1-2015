from turtle import *
#remember, the intersect function will use self.x, self.y but the function that check whether mario is on top of the mushroom uses bty. 

class Mario(Turtle):                                
	def __init__(self,canvas, lives, dx, dy,score,x,y, radius, bty, steps, stopfall,stopmove, stopjump):
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
		self.stopjump=stopjump
		self.speed(0)
	def move_right(self): #when stating that right key calls this function remember to make the if stetement to check whether x value is between  -500<x<-250 etc.
		if self.stopmove==False:		
			self.dx=10

		
	def move_left(self): 
		if self.stopmove==False:
			self.dx = -10
	def jump(self):
		#for a in range (1, 50):?
		if self.stopjump==False:
			self.stopfall=False
			self.dy=16
			self.bty=self.bty+self.dy
	def stopmario(self):		
		if self.bty==-100:
			self.stopfall=True

	def fall(self):
		if self.stopfall==False:
			self.dy=-1
			self.bty= self.bty+self.dy
	def get_radius(self):
		return self.radius

	def move(self):
		self.goto(self.xcor()+self.dx,self.ycor()+self.dy)
		self.dx=0
		self.dy=0

	def distance_increase(self):
		self.steps=self.steps+1
	def distance_decrease(self):
		self.steps=self.steps-1

	def dies(self):

		self.lives= self.lives-1
	def reach_top(self):
		if self.y==200:
			stopjump=True
		else: 
			stopjump=False
			 
#mario= Mario(lives=5, dx=5, dy=5, radius= 20, score=0, bty=-100, x=-400, y=-60, steps=0, canvas= screen, stopfall=False, stopmove=False)	
#turtle.penup()
#turtle.goto(-500,-100)
#turtle.pendown()
#turtle.goto(500,-100)
#turtle.mainloop()
