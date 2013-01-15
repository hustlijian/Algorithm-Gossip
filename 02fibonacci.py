#!/usr/bin/python

#filename: fibonacci.py
#date: 2013-01-05
#version: version 0.1
#description: count the Fibonacci num 
#like(sqquence 0,1,2,3,4) :
#    1, 1, 2, 3, 5, 8, 13

def fibonacci(n):
    if n<2: # 0, 1
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def main():
    n = raw_input('input the number:')
    n = int(n)
    print fibonacci(n)
    for i in xrange(10):
        print '%d: %d '%(i,fibonacci(i)),

if __name__ == '__main__':
    main()