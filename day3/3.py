f = open("3.txt", "r")
grid = [i.strip() for i in f]

#Part 1
def findPath(grid, steps):
	x, y = 0, 0
	rightStep, upStep = steps
	numLines = len(grid)
	lineWidth = len(grid[0])

	trees = 0
	while y < numLines:
		if grid[y][x] == "#":
			trees+= 1
		y += upStep 
		x = (x+rightStep)%lineWidth
	return trees

print(findPath(grid, (3, 1)))

#Part 2
def findPaths(grid, steps):
	total = 1
	for step in steps:
		total *= findPath(grid, step)
	return total 

steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print(findPaths(grid, steps))





