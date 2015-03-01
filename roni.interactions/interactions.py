import math()
def intersect(object1, object2):
	dist = math.sqrt((object1.xcor()-object2.xcor())**2 +(object1.ycor()-object2.ycor())**2)
