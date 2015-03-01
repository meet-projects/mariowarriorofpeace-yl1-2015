import turtle

screen= turtle.getscreen()
screen.register_shape("mario.gif")


class Mario(Turtle):
	def __init__(self,canvas, lives, dx, dy,score,x,y, radius, bty, steps):
		RawTurtle.__init(self, canvas)
	self.lives=lives
	self.penup()
	self.goto(x,y)
	self.x=x
	self.y=y
	self.dx=dx
	self.dy=dy
	self.shape("mario.gif")
	self.score=score
	self.radius= radius
	self.xloc= xloc
	self.bty= yloc
	self.steps=steps

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

mario= Mario(lives=5, dx=5, dy=5, radius= 20, score=0, bty=-100)	

turtle.mainloop()
