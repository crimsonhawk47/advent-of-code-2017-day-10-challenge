import os
from collections import defaultdict as dd
from time import process_time as pt


def ReturnPos(line):
    posx, posy = map(int, line.split('position=<')[1].strip(' ').rsplit('> ')[0].split(', '))
    velx, vely = map(int, line.split('velocity=<')[1].strip(' ').strip('>').split(', '))
    return [[posx,posy], [velx,vely]]


def GetMax(array, xma = -1e10, yma = -1e10, xmi = 1e10, ymi = 1e10):
    for pos, vel in array:
        xma = max(xma, pos[0])
        xmi = min(xmi,pos[0])
        yma = max(yma,pos[1])
        ymi = min(ymi,pos[1])
    return xma, xmi, yma, ymi


def FillDots(dMap): #Not Used
    for x in range(xmin, xmax+1):
        for y in range(ymin, ymax+1):
            dMap[x,y] = '.'
    return 0


def PrintMap(dMap, xmax, xmin, ymax, ymin):
    for y in range(ymin, ymax+1):
        for x in range(xmin, xmax + 1):
            print(dMap.setdefault((x,y),'.'), end = '')
        print('')

def PlaceCoords(dMap, test):
    for i in test:
        coordtoplace = tuple([i[0][0], i[0][1]])
        dMap.setdefault(coordtoplace,'#')
    return 0

def MoveCoordinates(test):
    global count
    for i in test:
        i[0] = [i[0][0] + i[1][0], i[0][1] + i[1][1]]
    count += 1



def RunRoutine(coords):
    MoveCoordinates(coords)
    xmax, xmin, ymax, ymin = GetMax(coords)
    return xmax, xmin, ymax, ymin



def RunRoutine2(coords):
    MoveCoordinates(coords)
    xmax, xmin, ymax, ymin = GetMax(coords)
    dMap = dd(tuple)
    PlaceCoords(dMap, coords)
    PrintMap(dMap, xmax, xmin, ymax, ymin)
    [print('') for i in range(2)]
    return 0


os.chdir(r'C:\Users\Gabriel\Desktop')
lines = open('.\Advent.txt').read().splitlines()
dMap = dd(tuple)
count = 0

def Main():
    coords = [ReturnPos(line) for line in lines]
    limits = GetMax(coords)
    
    while (limits[2]-limits[3]) > 19 and (limits[0]-limits[1])>60:
        limits = RunRoutine(coords)

    RunRoutine2(coords)
    print('Part 2 =',count)
    print('Ran for ', pt(),'seconds')
    return coords

coords = Main()
