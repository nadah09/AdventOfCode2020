from math import floor, ceil

f = open("5.txt", "r")
seats = f.read().split("\n")
seats = [i.strip() for i in seats[:-1]]

#Part1 
def findRowCol(seat):
	lowRow, highRow = 0, 127
	lowCol, highCol= 0, 7
	for i in range(7):
		mid = (lowRow+highRow)/2
		if seat[i] == "F":
			highRow = floor(mid)
		if seat[i] == "B":
			lowRow = ceil(mid)
	for i in range(7, 10):
		mid = (lowCol+highCol)/2
		if seat[i] == "L":
			highCol = floor(mid)
		if seat[i] == "R":
			lowCol = ceil(mid)
	return (lowRow, lowCol)

def findHighestSeat(seats):
	rowCols = [findRowCol(seat) for seat in seats]
	ids = [i[0]*8+i[1] for i in rowCols]
	return max(ids)

print(findHighestSeat(seats))

#Part 2
def findYourSeat(seats):
	rowCols = [findRowCol(seat) for seat in seats]
	ids = sorted([i[0]*8+i[1] for i in rowCols])[1:-1]
	for i in range(len(ids)-1):
		if ids[i+1] != ids[i]+1:
			return ids[i]+1

print(findYourSeat(seats))



