# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 17:31:37 2018

@author: aksha
"""

a = [ 10, 5, 15 ]
b = [ 20, 3, 2, 12 ]
n = len(a)
m = len(b)
 
# Final merge list
res = [0 for i in range(n + m)]
sortedMerge(a, b, res, n, m)
print "Sorted merged list "
 for i in range(n + m):
    print res[i]