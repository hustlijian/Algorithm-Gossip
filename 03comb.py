#!/usr/bin/python

#filename: comb.py
#date: 2013-01-05
#version: version 0.1
#description: show a trangele
#like:
      #                                            1    
      #                                         1      1    
      #                                     1      2      1    
      #                                 1      3      3      1    
      #                             1      4      6      4      1    
      #                         1      5     10     10      5      1    
      #                     1      6     15     20     15      6      1    
      #                 1      7     21     35     35     21      7      1    
      #             1      8     28     56     70     56     28      8      1    
      #         1      9     36     84    126    126     84     36      9      1    
      #     1     10     45    120    210    252    210    120     45     10      1    
      # 1     11     55    165    330    462    462    330    165     55     11      1    
# every elemnt is the situation number of select r items from n items: (n-r)!/r!
def combi(n, r):
    p = 1
    for x in xrange(1,r+1):
        p = p *(n-x+1)/x
    return p

def paint(N):
    for n in xrange(N):
        for r in xrange(N-n):
            print ' '*3,
        for i in xrange(n+1):
            print '%3d   '%combi(n,i),
        print ''

def main():
    paint(12)

if __name__ == '__main__':
    main()