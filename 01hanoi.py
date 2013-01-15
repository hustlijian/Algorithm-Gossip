#!/usr/bin/python

#filename: hanoi.py
#date: 2013-01-04
#version: version 0.1
#description: count the Towers of Hanoi


def hanoi(n, A, B, C):
    """move n sheet from A to C with the help of B"""
    if n==1:
        print 'move sheet %d from %c to %c'%(n, A, C)
    else:
        hanoi(n-1, A, C, B)
        print 'move sheet %d from %c to %c'%(n, A, C)
        hanoi(n-1, B, A, C)

def main():
    num = raw_input("input the sheet num:")
    try:
        num = int(num)
        hanoi(num, 'A', 'B', 'C')
    except Exception, e:
        print str(e)

if __name__ == '__main__':
    main()