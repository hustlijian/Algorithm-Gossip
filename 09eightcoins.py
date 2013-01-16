#!/usr/bin/python

#filename: 09eightcoins.py
#date: 2013-01-16
#version: version 0.1
#description: the eight coins puzzle
#       this is a determine way , just list the possible way

import random

def compare(coins, i, j, k):
    if coins[i] > coins[k]:
        print "fake coin %d heavier"%(i+1)
    else:
        print "fake coin %d lighter"%(j+1)

def eightcoins(coins):
    if coins[0]+coins[1]+coins[2] ==\
       coins[3]+coins[4]+coins[5]:
        if coins[6]>coins[7]:
            compare(coins, 6, 7, 0)
        else:
            compare(coins, 7, 6, 0)
    elif coins[0]+coins[1]+coins[2] >\
        coins[3]+coins[4]+coins[5]:
        if coins[0]+coins[3] == coins[1]+coins[4]:
            compare(coins, 2, 5, 0)
        elif coins[0] +coins[3]>coins[1]+coins[4]:
            compare(coins, 0, 4, 1)
        else:
            compare(coins, 1, 3, 0)
    else:
        if coins[0]+coins[3] == coins[1]+coins[4]:
            compare(coins, 5, 2, 0)
        elif coins[0] +coins[3]>coins[1]+coins[4]:
            compare(coins, 3, 1, 0)
        else:
            compare(coins, 4, 0, 1)

def main():
    coins = [10]*8 #init a list of eight 10
    randor = random.SystemRandom()
    # randor.randint(1, 10)
    weight = raw_input('fake weight(compare with 10):')
    try:
        weight = int(weight)
    except ValueError:
        print 'input a number'

    coins[randor.randint(0,7)] = weight

    eightcoins(coins)
    print'all the coins:'
    for i in xrange(0,8):
        print '%d'%coins[i],

if __name__ == '__main__':
    main()