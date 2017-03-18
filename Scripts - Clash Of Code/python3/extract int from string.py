import sys
import math
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

total = 0
n = int(input())
for i in range(n):
    test = input()
    searchObj = re.findall(r'\|\d+\|', test)
    total += len(searchObj)

print(total)

'''
n=popo1a18a36bbbdfbd2fbf999
sortie = 5
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

