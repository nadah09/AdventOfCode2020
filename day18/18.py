f = open("18.txt", "r")
math = f.read().split("\n")

#Part 1 
def findSum(math):
    sum_ = 0
    for eq in math:
        eq = process(eq)
        sum_ += compute(eq)
    return sum_

def process(eq):
    eq = eq.split(" ")
    neweq = []
    for i in eq:
        countopen = 0
        countclosed = 0
        while i[0] == "(":
            countopen += 1
            i = i[1:]
        while i[-1] == ")":
            countclosed +=1
            i = i[:-1]
        for j in range(countopen):
            neweq.append("(")
        neweq.append(i)
        for j in range(countclosed):
            neweq.append(")")
    return neweq

def compute(eq):
    symbols = "()+*"
    if "(" in eq:
        start = len(eq)-1
        end = start
        while eq[start] != "(":
            if eq[start] == ")":
                end = start
            start-=1
        mid = eq[start+1:end]
        left = eq[:start]
        right = eq[end+1:]
        return compute(left+[str(compute(mid))]+right)
    else:
        i = -2
        try:
            while eq[i] not in symbols:
                i-=1
        except:
            return int("".join(eq))
        num = int("".join(eq[i+1:]))
        if eq[i] == "+":
            return num + compute(eq[:i])
        elif eq[i] == "*":
            return num * compute(eq[:i])


#Part 2
def findSum2(math):
    sum_ = 0
    for eq in math:
        eq = process(eq)
        sum_ += compute2(eq)
    return sum_

def compute2(eq):
    symbols = "()+*"
    if "(" in eq:
        start = len(eq)-1
        end = start
        while eq[start] != "(":
            if eq[start] == ")":
                end = start
            start-=1
        mid = eq[start+1:end]
        left = eq[:start]
        right = eq[end+1:]
        return compute2(left+[str(compute2(mid))]+right)
    else:
        if "+" in eq:
            i = len(eq)-2
            try:
                while eq[i] != "+":
                    i-=1
            except:
                return int("".join(eq))
            mid = eq[i-1:i+2]
            left = eq[:i-1]
            right = eq[i+2:]
            sum_ = int(mid[0]) + int(mid[2])
            return compute2(left + [str(sum_)] + right)
        else:
            i = -2
            try:
                while eq[i] != "*":
                    i-=1
            except:
                return int("".join(eq))
            num = int("".join(eq[i+1:]))
            return num * compute2(eq[:i])


print(findSum(math))
print(findSum2(math))
