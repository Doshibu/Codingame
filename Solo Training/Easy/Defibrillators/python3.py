import sys
import math

def toFloat(pStr):
    return float(pStr.replace(',','.'));

userLng = toFloat(input())
userLat = toFloat(input())

dist = float("inf")
defib = ''

n = int(input())
for i in range(n):
    data=input().split(';')
    name=data[1]
    lng=toFloat(data[4])
    lat=toFloat(data[5])
    
    x = (userLng - lng) * math.cos((userLat + lat) / 2);
    y = (userLat - lat);
    d = math.sqrt(x*x + y*y) * 6371;
    
    if d<dist :
        dist=d
        defib=name

print(defib)
