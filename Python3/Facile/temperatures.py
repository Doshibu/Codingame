import sys
import math

n = int(input())  # the number of temperatures to analyse
if n==0:
    print(0)
else :
    temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526
    temps=temps.split(" ")
    
    closestP = 10001
    closestN = -10001
    for i in range(n) :
        temp = int(temps[i])
        if temp>0 and temp<closestP :
            closestP = temp
        elif temp<0 and temp>closestN :
            closestN = temp
            
    castN = closestN * -1
    if closestP == castN or closestP<castN :
        print(closestP)
    else :
        print(closestN)  
