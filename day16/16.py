f = open("16.txt", "r")
rules, yours, nearby = f.read().split("\n\n")
rules = rules.split("\n")
nearby = nearby.split("\n")[1:]
yours = yours.split("\n")[1:]

#Part 1
def findInvalid(rules, tickets):
    error = 0
    valid = findValidNums(rules)
    for ticketLine in tickets:
        tix3 = ticketLine.split(",")
        for ticket in tix3:
            if int(ticket) not in valid:
                error+= int(ticket)
    return error

def findValidNums(rules):
    possible = set()
    for rule in rules:
        field, vals = rule.split(": ")
        ranges = vals.split(" or ")
        for r in ranges:
            start, end = r.split("-")
            for i in range(int(start), int(end)+1):
                possible.add(i)
    return possible

#Part 2


print(findInvalid(rules, nearby))