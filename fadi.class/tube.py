from turtle import *
import tkinter.messagebox
import tkinter
import random
import math
screenMinX = -500
screenMinY = -500
screenMaxX = 500
screenMaxY = 500

screen = turtle.getscreen()
screen.register_shape("tube.gif")
turtle.penup()
turtle.shape("tube.gif")
turtle.goto(120,30)

#Here we DEFINE the class tube 
class tube(Turtle):
    # __init__ is going to be called per every new tube we create a new tube
    def __init__(self,canvas,dx,dy,x,y,size,ycor)
        RawTurtle.__init__(self,canvas) #this line keep it as it is
        # we define the properties of the tube
        self.penup()
        self.goto(x,y)
        self.size = size
        self.dx = dx
        self.dy = dy
        self.ycor=ycor
        
    def getSize(self):
        return self.size
    
    def getDX(self):
        return self.dx
    
    def getDY(self):
        return self.dy
    
    def setDX(self,dx):
        self.dx = dx
        
    def setDY(self,dy):
        self.dy = dy

    def appearrance(self.random x):
        random x = random.random() * 3 +1,sceenMinX < random x < screenMaxX
    def appearrance(self.random y):
        random y = random.random() * 3 +1,sceenMinY < random Y < screenMaxY

    
    def moveleft(self):        
        self.goto(x-self.dx,y)
   

   def tpy(self.tpy): 




#the tube's class is done 
     

turtle.mainloop()






















