f = open("3.txt", "r")
grid = [i.strip() for i in f]

#Part 1
def findTrees(grid, steps):
	dx, dy = steps
	rows, cols = len(grid), len(grid[0])
	i, j = 0, 0
	trees = 0
	while i < rows:
		val = grid[i][j%cols]
		if val == "#":
			trees += 1
		i += dy
		j += dx
	return trees

def findTotalPaths(grid, steps):
	total = 1
	for step in steps:
		total *= findTrees(grid, step)
	return total

steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print(findTrees(grid, (3, 1)))
print(findTotalPaths(grid, steps))





