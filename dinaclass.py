screenMinX= -500
screenMinY= -500
screenMaxX= 500
screenMaxY= 500
import turtle
screen= turtle.getscreen()
screen.register_shape("goodmushroom.gif")

class Good_mushrooms(Turtle):
	def __init__(self,canvas,x,y,dx,shape,radius):
		RawTurtle.__init__(self,canvas)
		self.penup()
		self.goto(x,y)
		self.dx = dx
		self.radius=radius
		self.shape("goodmushroom.gif")

	def getDX(self):
        		return self.dx
    
    def setDX(self,dx):
        				self.dx =dx
    
    def moveleft(self):
		 		x = self.xcor()
		 	    self.goto(x-dx,y)
    
    def getRadius(self):
        		return   self.radius
 

 dina=Good_mushrooms(x=10,y=10,dx=7,radius=10)
