f = open("2.txt", "r")
lines = [i.strip() for i in f]

def processLines(lines):
	processed = []
	for line in lines:
		rule, password = line.split(": ")
		rang, letter = rule.split(" ")
		first, last = [int(i) for i in rang.split("-")]
		processed.append([first, last, letter, password])
	return processed

#Part 1
def countValidPasswords(logs):
	count = 0
	for log in logs:
		first, last, letter, pw = log
		letterCount = pw.count(letter)
		if letterCount >= first and letterCount <= last:
			count += 1
	return count

#Part 2
def countValidPasswords2(logs):
	count = 0
	for log in logs:
		first, last, letter, pw = log
		letters = [pw[first-1], pw[last-1]]
		letterCount = letters.count(letter)
		if letterCount == 1:
			count += 1
	return count

lines = processLines(lines)
print(countValidPasswords(lines))
print(countValidPasswords2(lines))
