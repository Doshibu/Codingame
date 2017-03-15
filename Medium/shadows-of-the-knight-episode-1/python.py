import sys
import math

w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
X0, Y0 = [int(i) for i in input().split()]

xa=0; ya=0; xz=w-1; yz=h-1

while True:
    bombDir = input()
    
    if "R" in bombDir:
        xa=X0+1
                
    if "L" in bombDir:
        xz=X0-1
                
    if "D" in bombDir:
        ya=Y0+1
                    
    if "U" in bombDir:
        yz=Y0-1
                    
    X0 = int((xz-xa)//2) + xa
    Y0 = int((yz-ya)//2) + ya              
    print(str(X0)+" "+str(Y0))