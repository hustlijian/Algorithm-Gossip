#!/usr/bin/python

#filename: 08queen.py
#date: 2013-01-14
#version: version 0.1
#description: the eight queen puzzle

N = 8
column = [0 for i in range(N+1)] # 1 for have queen
rup = [0 for i in range(2*N+1)]
lup = [0 for i in range(2*N+1)]
queen = [0 for i in range(N+1)]
num = 0

def showAnswer():
    global num
    num += 1
    print 'answer %d'%num
    for x in xrange(1,N+1):
        for y in xrange(1,N+1):
            if queen[y] == x:
                print 'Q',
            else:
                print '.',
        print ''

def backtrack(i):
    global rup, lup , column
    if i > N:
        showAnswer()
        return

    for j in xrange(1,N+1):
        if column[j]==1 and rup[i+j]==1 and lup[i-j+N] == 1:
            queen[i] = j
            column[j] =rup[i+j] = lup[i-j+N] = 0
            backtrack(i+1)
            column[j] = rup[i+j] = lup[i-j+N] = 1

def main():
    global column
    global rup
    global lup
    for i in xrange(1,N+1):
        column[i] = 1

    for i in xrange(1,2*N+1):
        rup[i] = lup[i] = 1

    backtrack(1)

if __name__ == '__main__':
    main()