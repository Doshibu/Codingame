import sys
import math

while True:
    keys={}
    for i in range(8):
        mountain_h = int(input())
        keys[i]=mountain_h
        if i==7 : print(max(keys, key=keys.get))
