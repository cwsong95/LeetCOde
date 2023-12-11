# Imagine a robot standing at position (0,0) in a 2D grid, given a string consisting of it’s
#	moves, find the final location of the robot
# for example, input UD
#	U: up, increase in y axis
#	D: down, Decrease in y axis
#	R: right, increase in x axis 
# 	L: left, Decrease in x axis 
class Solution:
	def judgeCircle(self, moves: str) -> bool:
		x = 0
		y = 0
		for move in moves:
			if(move == 'U'):
				y += 1
			elif(move == 'D'):
				y -= 1
			elif(move == 'R'):
				x += 1
			elif(move == 'L'):
				x -= 1

		return x == 0 and y == 0