import random
import turtle
screen = turtle.getscreen()
screen.register_shape("Goomba2.gif")
turtle.shape("Goomba2.gif")


class bad_mashroom(Turtle):
        def __init__(self,canvas,dx,x,y,tpy,shape,radius):
          RawTurtle.__init__(self,canvas) 
          self.penup()
          self.goto(x,y)
          self.dx = dx

	        self.tpy = tpy
          self.shape("Goomba2.gif")
	        self.radius=radius
        def getDX(self):
       		return self.dx
    
 
    
        def setDX(self,dx):
   	      self.dx = dx
       
	

	      def move_left(self):
	        self.dx=-20

        def move(self):
          self.goto(self.xcor()+self.dx, self.ycor())
          self.dx=-10

        def die(self):
          self.hide

       
