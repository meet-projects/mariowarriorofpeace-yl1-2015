import math()
#stop.xmove=False #when mario is bumping into the tube
#stop.fall=False #when mario is on tube this will be True
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


		elif:
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
		
