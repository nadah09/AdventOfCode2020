from math import floor, ceil

f = open("5.txt", "r")
seats = f.read().split("\n")
seats = [i.strip() for i in seats[:-1]]

#Part 1
def findMax(seats):
	maxSeat = 0
	for seat in seats:
		num = findSeatNum(seat)
		maxSeat = max(maxSeat, num)
	return maxSeat

def findSeatNum(seat):
	#seats = ["FBFBBFFRLR"]
	r, c = seat[:7], seat[7:]
	row = findRow(r)
	col = findCol(c)
	return row*8+col

def findRow(row):
	l = 0
	r = 127
	for direction in row:
		mid = (l+r)//2
		if direction == "F":
			r = mid
		if direction == "B":
			l = mid
	return r

def findCol(col):
	l = 0
	r = 7
	for direction in col:
		mid = (l+r)//2
		if direction == "L":
			r = mid
		if direction == "R":
			l = mid
	return r

#Part 2
def findYourSeat(seats):
	seen = set()
	for seat in seats:
		num = findSeatNum(seat)
		seen.add(num)
	for seat in seen:
		if seat + 1 not in seen and seat+2 in seen:
			return seat+1
	return 0

print(findMax(seats))
print(findYourSeat(seats))



