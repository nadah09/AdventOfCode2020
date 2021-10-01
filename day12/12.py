import math
from math import cos, sin
f = open("12.txt", "r")
dirs = f.read().split("\n")[:-1]
dirs = [i.strip() for i in dirs]

#Part 1
def findManhattanDistance(dirs):
    x, y, th, dx, dy = 0, 0, 0, 1, 0
    turns = {"L", "R"}
    cardinal = {"N", "S", "E", "W"}
    forward = "F"
    for d in dirs:
        command, num = d[0], int(d[1:])
        if command in turns:
            th, dx, dy = turn(command, num, th, dx, dy)
        elif command in cardinal:
            x, y = moveDirection(command, num, x, y)
        elif command == forward:
            x, y = moveForward(num, dx, dy, x, y)
    return abs(x) + abs(y)

def moveDirection(command, num, x, y):
    if command == "N":
        y += num
    if command == "S":
        y -= num
    if command == "E":
        x += num
    if command == "W":
        x -= num
    return x, y

def turn(command, num, th, dx, dy):
    if command == "L":
        th = (th+num)%360
    if command == "R":
        th = (th-num)%360
    dx, dy = int(cos(math.radians(th))), int(sin(math.radians(th)))
    return th, dx, dy

def moveForward(num, dx, dy, x, y):
    x += num*dx
    y += num*dy
    return x, y

#Part 2
def findWayPointManhattanDistance(dirs):
    x, y, th = 0, 0, 0
    wx, wy = 10, 1
    turns = {"L", "R"}
    cardinal = {"N", "S", "E", "W"}
    forward = "F"
    for d in dirs:
        command, num = d[0], int(d[1:])
        if command in turns:
            wx, wy = rotateWayPoint(command, num, wx, wy)
        elif command in cardinal:
            wx, wy = moveDirection(command, num, wx, wy)
        elif command == forward:
            x, y = moveToWayPoint(num, x, y, wx, wy)
    return abs(x)+abs(y)

def moveToWayPoint(num, x, y, wx, wy):
    for n in range(num):
        x += wx
        y += wy
    return x, y

def rotateWayPoint(command, th, wx, wy):
    if command == "R":
        th = (-th)%360
    dx, dy = int(cos(math.radians(th))), int(sin(math.radians(th)))
    if dx == -1:
        wx *= -1
        wy *= -1
    elif dy == 1:
        wx, wy = -wy, wx
    elif dy == -1:
        wx, wy = wy, -wx
    return wx, wy


print(findManhattanDistance(dirs))
print(findWayPointManhattanDistance(dirs))



