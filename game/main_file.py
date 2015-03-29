#This is a demo project for meet Yearlong 2014-15 Y1
from turtle import *
import tkinter.messagebox
import tkinter
import random
import math
#from dinaclass import *

from roniclass import Mario
#from interactions import * 
#from tamar import bad_mashroom
#from paditube import tube 
#from cloud import cloud

#These Four variables are the borders of the game world
screenMinX = -500
screenMinY = -500
screenMaxX = 500
screenMaxY = 500

def intersect(object1, object2):
	dist = math.sqrt((object1.xcor()-object2.xcor())**2 +(object1.ycor()-object2.ycor())**2)

	if dist <= radius1 + radius2:
		return True
	else:
		return False

def intersect_check():
	
	if intersect(Mario, bad_mashroom):
		if Mario.bty>=bad_mashroom.tpy:
			die(bad_mashroom)#remind tamar to make the function!
		else:
			die(Mario)
			Mario.goto(-500,-100)

	if intersect(Mario, Good_mushrooms):
		die(Good_musrhooms)

	if intersect(Mario, tube):
		
		if Mario.bty<tube.tpy:
			stop.xmove=True
	
	if intersect(Mario, hole):
		
		if Mario.bty<=-100:
			die(Mario)

def main():
    # These 4 lines just to prepare the window of the game, no need to change them
    root = tkinter.Tk()
    root.title("mario roni gever")
    cv = ScrolledCanvas(root,600,600,600,600)
    cv.pack(side = tkinter.LEFT)

    #Here we prepre the new shapes of the game
    t = RawTurtle(cv)
    screen = t.getscreen()
    screen.setworldcoordinates(screenMinX,screenMinY,screenMaxX,screenMaxY)
    screen.register_shape("hole1",((250,-500),(250,-400),(150,-400),(150,-500)))
    screen.register_shape("hole2",((250,-500),(250,-400),(100,-400),(100,-500)))
    screen.register_shape("hole3",((250,-500),(250,-400),(200,-400),(200,-500)))
    screen.register_shape("goodmario.gif")
    screen.register_shape("cloud.gif")
    screen.register_shape("goodmushrooms.gif")
    screen.register_shape("tube.gif")
    frame = tkinter.Frame(root)
    frame.pack(side = tkinter.RIGHT,fill=tkinter.BOTH)
    t.ht()
    
    # this function when it is called the game will exit
    def quitHandler():
        root.destroy()
        root.quit()

    #here we are creating the button that you will see it on the right side of the game called Quit
    # the part it says command=quitHandler is telling the button when we click it to run the function quitHandler that we defined above
    quitButton = tkinter.Button(frame, text = "Quit", command=quitHandler)
    quitButton.pack()
    
    screen.tracer(10)
    

    #shown_goodmushrooms= []

    #for a in range(2):
    # here we are using the class we defined above to create the spaceShip
    #	goodmushroom= Good_mushrooms(x=500,y=-70,canvas=screen,dx=5, radius=20)
    #	shown_goodmushrooms.append(goodmushroom)


    #hidden_goodmushrooms= []

    #for a in range(2):
    	#x=random.random()*(screenMaxX-screenMinx)+screenMinX
    #	goodmushroom= Good_mushrooms(x=500, y=-70, canvas=screen, dx=5, radius=20)	
    #	hidden_goodmushrooms.append(goodmushroom)
    # This is preparing a list that we will store all the astroids in it
    
    #shown_badmushrooms= []

    #for b in range(4):
    # here we are using the class we defined above to create the spaceShip
    #	badmushroom= bad_mashrooms(x=500,y=-70,canvas=screen,dx=5, radius=20)
    #	shown_badmushrooms.append(badmushroom)


    #hidden_badmushrooms= []

    #for b in range(4):
    #	badmushroom= bad_mashrooms(x=500, y=-70, canvas=screen, dx=5, radius=20)	
    #	hidden_badmushrooms.append(badmushroom)
    # this loop runs 5 times and each time it creates an astroid and adds it to the list of astroids
    #shown_tubes=[]
    #for c in range (2)
     #   tubes=tube(canvas=screen.x=500,y=-70,dx=5,radius=20)
      #  shown_tubes.append(tubes)
    
    #hidden_tubes=[]
    #for c in range (2)
     #   tubes=tube(canvas=screen.x=500,y=-70,dx=5,radius=20)
      #  hidden_tubes.append(tubes)

#    shown_holes=[]
 #   for d in range (3)

  #  	size= random.radom()*3 +1
   #     hole=Holes(canvas=screen.x=500,y=-70,dx=5,radius=20,int(size))
    #    shown_holes.append(hole)
    #hidden_holes=[]
    #for d in range (3)
    #    size= random.radom()*3 +1
    #    hole=Holes(canvas=screen.x=500,y=-70,dx=5,radius=20,int(size))
     #   hidden_holes.append(hole)

    mario= Mario(lives=5, dx=0, dy=0, radius= 20, score=0, bty=-100, x=0, y=0, steps=0, canvas= cv, stopfall=True, stopmove=False, stopjump=False)
    def play():
    	#print("hello")
    	mario.move()
    	mario.fall()
    	mario.stopmario()
    	screen.ontimer(play, 5)
        # Tell all the elements of the game to move
        # Tell the ship to move
        #ship.move()
        # go (loop) though each astroid in the astroids list and tell it to move as well check if it is toucing the ship
        #for goodmushroom in shown_goodmushrooms:

        #for badmushroom in shown_badmushrooms:

        #for hole in shown_holes:

        #for tube1 in shown_tubes:
        #    if (intersect(mario,tube1)):
        #        print("You Failed")
        #        quitHandler()
        #    asteroid.move()
        # Set the timer to go off again in 5 milliseconds
    # GAME LOOP (ENDS)

    # Set the timer to go off the first time in 5 milliseconds
    screen.ontimer(play,1)
    # this means call the defined function in class spaceShip turrnLeft for the ship everytime the left arrow key is pushed in the keyboard
    screen.onkeypress(mario.move_left,"Left")
    # this means call the defined function in class spaceShip turrnRight for the ship everytime the right arrow key is pushed in the keyboard
    screen.onkeypress(mario.move_right,"Right")
    # this means call the defined function in class spaceShip turrnLeft for the ship everytime the up arrow key is pushed in the keyboard
    screen.onkeypress(mario.jump,"Up")
    
    screen.listen()
    tkinter.mainloop()
  
if __name__ == "__main__":
    main()