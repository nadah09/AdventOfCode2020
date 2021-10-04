f = open("25.txt", "r")
card, door = [int(i) for i in f.read().split("\n")]
print(card, door)

#Part 1
def findEncryptionKey(card, door, subj):
    cardloop = findLoop(subj, card)
    doorloop = findLoop(subj, door)
    start = door
    for i in range(cardloop-1):
        start*=door
        start = start%20201227
    return start

def findLoop(subj, public):
    start = subj
    i = 0
    while start != public:
        i+= 1
        start*=subj
        start = start%20201227
    return i+1

print(findEncryptionKey(card, door, 7))
