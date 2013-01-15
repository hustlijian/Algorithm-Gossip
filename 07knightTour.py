#!/usr/bin/python

#filename: 07knightTour.py
#date: 2013-01-08
#version: version 0.1
#description: the Knight tour puzzle

board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ]

def travel(x, y):
    ktmove1 = [-2, -1, 1, 2, 2, 1, -1, -1]
    ktmove2 = [1, 2, 2, 1, -1, -2, -2, -1]

    nexti = [0, 0, 0, 0, 0, 0, 0, 0]
    nextj = [0, 0, 0, 0, 0, 0, 0, 0]
    exists = [0, 0, 0, 0, 0, 0, 0, 0]

    i = x
    j = y
    k = 0
    m = 0
    l = 0
    tempi = 0
    tempj = 0
    count = 0
    min = 0
    tmp = 0

    board[i][j] = 1

    for m in xrange(2,65):
        for l in xrange(0,8):
            exists[l] = 0
        l = 0

        # try the eight direction
        for k in xrange(0,8):
            tempi = i + ktmove1[k]
            tempj = j + ktmove2[k]

            if tempi<0 or tempj <0 or tempi>7 or tempj > 7:
                continue
            if board[tempi][tempj] == 0:
                nexti[l] = tempi
                nextj[l] = tempj
                l += 1

        count = l
        if count == 0:
            return 0
        if count == 1:
            min = 0
        else:
            for l in xrange(0,count):
                for k in xrange(0,8):
                    tempi = nexti[l] + ktmove1[k]
                    tempj = nextj[l] + ktmove2[k]
                    if tempi <0 or tempj <0 or tempi > 7 or tempj >7:
                        continue
                    if board[tempi][tempj] == 0:
                        exists[l]+=1
            tmp = exists[0]
            min = 0
            for l in xrange(1,count):
                if exists[l] < tmp:
                    tmp = exists[l]
                    min = l
        i = nexti[min]
        j = nextj[min]
        board[i][j] = m

    return 1

def main():
    startx = 1
    starty = 1

    if travel(startx, starty):
        print 'ok'
    else:
        print 'fail'

    for i in xrange(0,8):
        for j in xrange(0,8):
            print '%2d'%board[i][j],
        print ''
    return 0

if __name__ == '__main__':
    main()