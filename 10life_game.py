#!/usr/bin/python

#filename: 10life_game.py
#date: 2013-01-17
#version: version 0.1
#description: the game of life
# 0,1,4,5,6,7,8: to dead
# 2: to be still
# 3.: to be alive

from time import sleep as Sleep

MAXROW = 10
MAXCOL = 25
DEAD = 0
ALIVE = 1

class LifeGame:
    oldmap = [[0 for x in xrange(MAXCOL)] for x in xrange(MAXROW)] 
    newmap = [[0 for x in xrange(MAXCOL)] for x in xrange(MAXROW)] 

    def __init__(self):
        self.init()

    def init(self):
        row = 0
        col = 0
        for row in xrange(0,MAXROW):
            for col in xrange(0,MAXCOL):
                self.oldmap[row][col] = DEAD

        print 'enter x, y where x,y is living cell 0<=x<=%d, 0<=y<=%d'\
            %(MAXROW-1, MAXCOL-1)
        print 'end with x,y=-1, -1'
        
        while True:
            try:
                row = int(raw_input('x:'))
                col = int(raw_input('y:'))
            except Exception, e:
                print  str(e)         
                break   

            if 0<=row and row <MAXROW and 0<=col and col<MAXCOL:
                self.oldmap[row][col] = ALIVE
            elif row == -1 and col == -1:
                break
            else:
                print '(x, y) exceeds map range!'

    def neighbors(self, row, col):
        count = 0
        for r in xrange(row-1,row+2):
            for c in xrange(col-1,col+2):
                if r<0 or r>=MAXROW or c<0 or c >=MAXCOL:
                    continue
                if self.oldmap[r][c] == ALIVE:
                    count += 1
        if self.oldmap[row][col] == ALIVE:
            count -= 1
        return count
    def output_map(self):
        for row in xrange(0,MAXROW):
            for col in xrange(0,MAXCOL):
                if self.oldmap[row][col] == ALIVE:
                    print '#',
                else:
                    print '-',
            print ''
        # print self.oldmap
        print '*'*MAXCOL*2

    def copy_map(self):
        for row in xrange(0,MAXROW):
            for col in xrange(0,MAXCOL):
                self.oldmap[row][col] = self.newmap[row][col]

    def run(self):
        while self.isStop() :
            print self.isStop() #Debug
            self.output_map()
            for row in xrange(0,MAXROW):
                for col in xrange(0,MAXCOL):
                    num = self.neighbors(row, col)
                    if num == 2:
                        self.newmap[row][col]= self.oldmap[row][col]
                    elif num == 3:
                        self.newmap[row][col] = ALIVE
                    else:
                        self.newmap[row][col] = DEAD

            self.copy_map()
            Sleep(0.5)
            

    def isStop(self):
        count = 0
        for row in xrange(0,MAXROW):
            for col in xrange(0,MAXCOL):
                if self.oldmap[row][col] == ALIVE:
                   count += 1
        return count

def main():
    game = LifeGame()
    game.run()

if __name__ == '__main__':
    main()