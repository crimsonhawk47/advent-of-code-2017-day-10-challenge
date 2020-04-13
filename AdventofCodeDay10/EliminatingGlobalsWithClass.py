import os
from time import process_time as pt
from collections import defaultdict as dd
os.chdir(r'C:\Users\Gabriel\Desktop')


class TestClass(object):
    def __init__(self):
        lines = open(r'.\Advent.txt').read().splitlines()
        self.coords = [self.returnpos(line) for line in lines]
        self.count = 0
        self.count2 = self.count
        self.limits = 1e5,-1e6,1e5,-1e6

    def returnpos(self, line):
        posx, posy = map(int, line.split('position=<')[1].strip(' ').rsplit('> ')[0].split(', '))
        velx, vely = map(int, line.split('velocity=<')[1].strip(' ').strip('>').split(', '))
        return [[posx, posy], [velx, vely]]

    def getmax(self, array, xma = -1e10, yma = -1e10, xmi = 1e10, ymi = 1e10):
        for pos, vel in array:
            xma = max(xma, pos[0])
            xmi = min(xmi,pos[0])
            yma = max(yma,pos[1])
            ymi = min(ymi,pos[1])
            self.limits = xma, xmi, yma, ymi

    def printMap(self, dMap):
        for y in range(self.limits[3], self.limits[2]+1):
            for x in range(self.limits[1], self.limits[0]+1):
                print(dMap.setdefault((x,y),'.'), end = '')
            print('')

    def placeCoords(self, dMap):
        for i in self.coords:
            coordtoplace = tuple([i[0][0], i[0][1]])
            dMap.setdefault(coordtoplace,'#')

    def MoveCoordinates(self, test):
        for i in test:
            i[0] = [i[0][0] + i[1][0], i[0][1] + i[1][1]]
        self.count += 1

    def RunRoutine(self):
        self.MoveCoordinates(self.coords)
        self.getmax(self.coords)
        return self.limits

    def RunRoutine2(self):
        print('xrange is ', self.limits[0]-self.limits[1], 'and y range is', self.limits[2]-self.limits[3])
        self.MoveCoordinates(self.coords)
        self.getmax(self.coords)
        print('xrange is ', self.limits[0]-self.limits[1], 'and y range is', self.limits[2]-self.limits[3])
        dMap = dd(tuple)
        self.placeCoords(dMap)
        self.printMap(dMap)
        [print('') for i in range(2)]
        return 0
    def Main(self):
        while self.limits[2] - self.limits[3] > 19 and self.limits[0] - self.limits[1] > 60:
            self.RunRoutine()
        self.RunRoutine2()
        return self.count


t = TestClass()

t.Main()
print('Part 2 =', t.count)
print('Ran for ', pt(), 'seconds')
