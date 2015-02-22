import turtle

screen= turtle.getscreen()
screen.register_shape("mario.gif")


class Mario(Turtle):
	def __init__(self,canvas, lives, dx, dy,score,x,y)
		RawTurtle.__init(self, canvas)

	self.penup()
	self.goto(x,y)
	self.x=x
	self.y=y
	self.dx=dx
	self.dy=dy
	self.shape("mario.gif")
	self.score=score

	def move_right(self.x, self.y): #when stating that right key calls this function remember to make the if stetement to check whether x value is between  -500<x<-250 etc.
				
		self.goto(self.x+self.dx, self.y)
	def move


turtle.mainloop()
