from copy import deepcopy

f = open("11.txt", "r")
seats = f.read().split("\n")
seats = [[j for j in i] for i in seats]

#Part 1
def seatChanges(seats):
	count = 0
	while True:
		changed, seats = updateSeats(seats)
		if changed > 0:
			count += 1
		else:
			return findOccupied(seats)

def findOccupied(seats):
	count = 0
	for row in seats:
		count += sum([1 if i == "#" else 0 for i in row])
	return count

def findNeighbors(seats, i, j):
	neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1), (i+1, j+1), (i+1, j-1), (i-1, j+1), (i-1, j-1)]
	neighbors = [(x, y) for x, y in neighbors if x >= 0 and y >= 0 and x < len(seats) and y < len(seats[0])]
	occupied = sum([1 if seats[x][y] == "#" else 0 for x, y in neighbors])
	return occupied


def updateSeats(seats):
	toChange = 0
	prev = deepcopy(seats)

	for i in range(len(seats)):
		for j in range(len(seats[0])):
			current = seats[i][j]
			if current == ".":
				continue
			occupied = findNeighbors(prev, i, j)
			if current == "#" and occupied >= 4:
				seats[i][j] = "L"
				toChange += 1
			elif current == "L" and occupied == 0:
				seats[i][j] = "#"
				toChange += 1
	return toChange, seats

#Part 2
def seatChanges2(seats):
	count = 0
	while True:
		changed, seats = updateSeats2(seats)
		if changed > 0:
			print(changed)
			count += 1
		else:
			return findOccupied(seats)

def updateSeats2(seats):
	toChange = 0
	prev = deepcopy(seats)

	for i in range(len(seats)):
		for j in range(len(seats[0])):
			current = seats[i][j]
			if current == ".":
				continue
			occupied = findNeighbors2(prev, i, j)
			if current == "#" and occupied >= 5:
				seats[i][j] = "L"
				toChange += 1
			elif current == "L" and occupied == 0:
				seats[i][j] = "#"
				toChange += 1
	return toChange, seats

def findNeighbors2(seats, i, j):
	count = 0
	directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
	for d in directions:
		x, y = i+d[0], j+d[1]
		while x >= 0 and y>=0 and x < len(seats) and y < len(seats[0]):
			if seats[x][y] != ".":
				if seats[x][y] == "#":
					count += 1
				break
			x += d[0]
			y += d[1]
	return count

		



print(seatChanges(seats))
print(seatChanges2(seats))