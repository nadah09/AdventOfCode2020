f = open("16.txt", "r")
rules, yours, nearby = f.read().split("\n\n")
rules = rules.split("\n")
nearby = nearby.split("\n")[1:]
yours = yours.split("\n")[1:]

#Part 1
def findInvalid(rules, tickets):
    error = 0
    newTickets = []
    count = 0
    valid = findValidNums(rules)
    for ticketLine in tickets:
        add = True
        tix3 = ticketLine.split(",")
        for ticket in tix3:
            if int(ticket) not in valid:
                error+= int(ticket)
                count += 1
                add = False
                continue
        if add:
            newTickets.append(tix3)
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
def matchCategories(rules, tickets, yours):
    yours = [int(i) for i in yours[0].split(",")]
    tickets = cleanTickets(rules, tickets)
    rules = parseRules(rules)
    fieldRanges = findIdxRanges(tickets)
    fieldToIdx = findFields(rules, fieldRanges)
    product = 1
    for field in fieldToIdx:
        if "departure" in field:
            idx = list(fieldToIdx[field])[0]
            product*=yours[idx]
    return product


def cleanTickets(rules, tickets):
    newTickets = []
    valid = findValidNums(rules)
    for ticketLine in tickets:
        add = True
        tix3 = ticketLine.split(",")
        for ticket in tix3:
            if int(ticket) not in valid:
                add = False
        if add:
            newTickets.append(tix3)
    return newTickets

def parseRules(rules):
    categoryToNums = {}
    for rule in rules:
        field, vals = rule.split(": ")
        ranges = vals.split(" or ")
        for r in ranges:
            start, end = [int(i) for i in r.split("-")]
            for i in range(start, end+1):
                try:
                    categoryToNums[field].add(i)
                except:
                    categoryToNums[field] = {i}
    return categoryToNums

def findIdxRanges(tickets):
    numFields = len(tickets[0])
    idxToNums = {}
    for ticket in tickets:
        for field in range(len(ticket)):
            try:
                idxToNums[field].add(int(ticket[field]))
            except:
                idxToNums[field] = {int(ticket[field])}
    return idxToNums

def findFields(rules, idxRanges):
    fieldToIdx = {}
    for i in rules:
        fieldToIdx[i] = set([j for j in range(len(rules))])
    for idx in idxRanges: #go through each index of tickets
        nums = idxRanges[idx] #go through all numbers in this index
        for num in nums:
            for field in rules: #go through all possible field ranges
                if num not in rules[field]:
                    fieldToIdx[field].remove(idx)
    fieldToIdx = clean(fieldToIdx)
    return fieldToIdx

def clean(fieldToIdx):
    toClean = True
    while toClean:
        toClean = False
        for field in fieldToIdx:
            if len(fieldToIdx[field]) == 1:
                idx = list(fieldToIdx[field])[0]
                for f2 in fieldToIdx:
                    if f2 != field:
                        try:
                            fieldToIdx[f2].remove(idx)
                        except:
                            continue
            else:
                toClean = True
    return fieldToIdx

print(findInvalid(rules, nearby))
print(matchCategories(rules, nearby, yours))