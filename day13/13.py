f = open("13.txt", "r")
begin, buses, _ = f.read().split("\n")
buses = [i for i in buses.split(",")]
begin = int(begin)

#Part 1
def findWaitTime(begin, buses):
    curr = begin
    buses = [int(i) for i in buses if i != "x"]
    while True:
        for bus in buses:
            if curr%bus == 0:
                return bus*(curr-begin)
        curr += 1
    return 0

#Part 2
def findConsecutiveBuses(buses):
    diff = makeDiffDict(buses)
    curr = 0
    skip = diff[0]
    seen = {diff[0]}
    while True:
        found = True
        for d in diff:
            bus = diff[d]
            if (curr+d)%bus != 0:
                found = False
                break
            else:
                if bus not in seen:
                    seen.add(bus)
                    skip*= bus
        if found:
            return curr
        curr += skip


def makeDiffDict(buses):
    times = {}
    for i in range(len(buses)):
        bus = buses[i]
        try:
            bus = int(bus)
            times[i] = bus
        except:
            continue
    return times

print(findWaitTime(begin, buses))
print(findConsecutiveBuses(buses))
