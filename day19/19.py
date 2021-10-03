f = open("19.txt", "r")
rules, passwords = f.read().split("\n\n")
rules = rules.split("\n")
passwords = passwords.split("\n")

#Part 1
def makeDict(rules):
    rulesToChars = {}
    for rule in rules:
        rulenum, options = rule.split(": ")
        rulenum = int(rulenum)
        options = options.split(" | ")
        #print(options)
        for option in options:
            if option[0] == "\"":
                rulesToChars[rulenum] = option[1:-1]
            else:
                try:
                    rulesToChars[rulenum].append([int(i) for i in option.split(" ")])
                except:
                    rulesToChars[rulenum] = [[int(i) for i in option.split(" ")]]   
    return rulesToChars

def findValidStrings(rules, start = 0):
    if type(rules[start]) != list:
        return [rules[start]]
    else:
        result = []
        for option in rules[start]:
            strings = [findValidStrings(rules, option[i]) for i in range(len(option))]
            while len(strings) >= 2:
                temp = []
                one = strings[0]
                two = strings[1]
                for s1 in one:
                    for s2 in two:
                        temp.append(s1+s2)
                strings = [temp] + strings[2:]
            for i in strings[0]:
                result.append(i)
        return result


def findValidPasswords(rules, passwords):
    rules = makeDict(rules)
    validStrings = findValidStrings(rules)
    count = 0
    for p in passwords:
        if p in validStrings:
            count += 1
    return count

#Part 2
def findValidStrings2(rules, start = 0, memo = None):
    if not memo:
        memo = {}
    if type(rules[start]) != list:
        return [rules[start]]
    else:
        print("HERE", start)
        result = []
        for option in rules[start]:
            for o in option:
                if o not in memo:
                    memo[o] = findValidStrings2(rules, o, memo)
            strings = [memo[option[i]] for i in range(len(option))]
            while len(strings) >= 2:
                temp = []
                one = strings[0]
                two = strings[1]
                for s1 in one:
                    for s2 in two:
                        temp.append(s1+s2)
                strings = [temp] + strings[2:]
            for i in strings[0]:
                result.append(i)
        return result

def findValidPasswords2(rules, passwords):
    rules = makeDict(rules)
    validStrings = findValidStrings2(rules)
    count = 0
    for p in passwords:
        if p in validStrings:
            count += 1
    return count



#print(findValidPasswords(rules, passwords))
print(findValidPasswords2(rules, passwords))
