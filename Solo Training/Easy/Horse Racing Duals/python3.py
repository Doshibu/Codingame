import sys
import math

n = int(input())
list=[]
for i in range(n):
    pi = int(input())
    if pi>0 and pi!='': 
        list.append(pi)

list.sort()

minDiff=list[1]-list[0]
for i in range(1, len(list)):
    diff=list[i]-list[i-1]
    if diff<minDiff: minDiff=diff
    
print(minDiff)
