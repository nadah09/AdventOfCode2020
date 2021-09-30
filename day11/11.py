f = open("11.txt", "r")
seats = f.read().split("\n")
seats = [i.split() for i in seats]
print(seats)

#Part 1
def seatChanges(seats):
	changing = True
	totalChanges = 0
	while changing:
		toChange = set()
		for seat in seats:
			pass



print(seatChanges(seats))