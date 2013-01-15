#!/usr/bin/python

#filename: 05maze.py
#date: 2013-01-07
#version: version 0.1
#description: a maze game

maze = [
    [2, 2, 2, 2, 2, 2, 2],
    [2, 0, 0, 0, 0, 0, 2],
    [2, 0, 2, 0, 2, 0, 2],
    [2, 0, 0, 2, 0, 2, 2],
    [2, 2, 0, 2, 0, 2, 2],
    [2, 0, 0, 0, 0, 0, 2],
    [2, 2, 2, 2, 2, 2, 2]
]

startI = 5
startJ = 1
endI = 1
endJ = 5
success = 0

def visit(i, j):
    global success
    maze[i][j] = 1

    if i==endI and j==endJ:
        success = 1;

    if success != 1 and maze[i][j+1] == 0:
        visit(i,j+1)
    if success != 1 and maze[i+1][j] == 0:
        visit(i+1, j)
    if success != 1 and maze[i][j-1] == 0:
        visit(i,j-1)
    if success != 1 and maze[i-1][j] == 0:
        visit(i-1, j)

    if success != 1:
        maze[i][j] = 0
    return success

def show_maze():
    for i in xrange(0,7):
        for j in xrange(0,7):
            if maze[i][j] == 2:
                print '*',
            elif maze[i][j] == 1:
                print '+',
            else:
                print ' ',
        print ''

def main():
    print 'the maze:'
    show_maze()

    if visit(startI,startJ) == 0:
        print ' no way'
        return

    print 'the maze way:'
    show_maze()

if __name__ == '__main__':
    main()