import sys
import math

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

mimeMap = {}
def getMimeType ( fileName ):
    qArray = fileName.split(".")
    if len(qArray) > 1 :
        extension = qArray.pop().lower()
        #print(extension + "  "+ str(mimeMap))
        if extension in mimeMap :
            return (mimeMap[extension])
    return "UNKNOWN"

for i in range(n) :
    lineN = input().split()
    mimeMap[lineN[0].lower()] = lineN[1]

for j in range(q) :
    print (getMimeType(input()))
