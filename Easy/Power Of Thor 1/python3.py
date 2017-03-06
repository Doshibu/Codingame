import sys
import math

lightX, lightY, thorX, thorY = [int(i) for i in input().split()]

while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    direction='';
    
    if(thorY > lightY):
        direction = "N"
        thorY-=1
    elif(thorY < lightY):
        direction = "S"
        thorY+=1
       
    if(thorX > lightX):
        direction += "W"
        thorX-=1
    elif(thorX < lightX):
        direction += "E"
        thorX+=1
    
    print(direction)
