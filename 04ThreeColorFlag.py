#!/usr/bin/python

#filename: ThreeColorFlag.py
#date: 2013-01-06
#version: version 0.1
#description: move the three colors flag to the order:
# Blue White Red, in least step without creat new array

BLUE = 'b'
WHITE = 'w'
RED = 'r'
total = 0

def swap(color_list,x, y):
    global total
    temp = color_list[x]
    color_list[x] = color_list[y]
    color_list[y] = temp
    total += 1

def main():
    color = ['r', 'w', 'b', 'w', 'w','b', 'r', 'b', 'w', 'r']
    wFlag = 0
    bFlag = 0
    rFlag = len(color)-1

    for i in color: # show the color_list
        print i,
    print ''

    while wFlag <= rFlag:
        if color[wFlag] == WHITE:
            wFlag += 1    
        elif color[wFlag] == BLUE:
            swap(color, bFlag, wFlag)
            bFlag += 1
            wFlag += 1
        else:
            while wFlag < rFlag and color[rFlag] == RED:
                rFlag -= 1
            swap(color, rFlag, wFlag)
            rFlag -= 1

    for i in color:
        print i,
    print ''

    print 'total : %d'%total
if __name__ == '__main__':
    main()