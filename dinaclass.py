screenMinX= -500
screenMinY= -500
screenMaxX= 500
screenMaxY= 500
class Good_mushrooms(Turtle):
	def __init__(self,canvas,x,y,dx,dy,shape):
		RawTurtle.__init__(self,canvas)
		self.penup()
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.shape("goodmushroom.gif")
