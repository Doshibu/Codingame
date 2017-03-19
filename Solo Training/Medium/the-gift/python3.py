import sys
import math

class Oods:
    def __init__(self, pBudget=0, pAmount=0):
        self.Budget=pBudget
        self.Amount=pAmount
    def __repr__(self):
        return repr((self.Budget, self.Amount))
    
n = int(input())
c = int(input())
listOods=[]

for i in range(n):
    b = int(input())
    listOods.append(Oods(int(b)))
    
amountLeft=int(c)
sortedOods=sorted(listOods, key=lambda x: x.Budget)

for i in range(len(sortedOods)):
    currentOod = sortedOods[i]
    amountPerOod = amountLeft / (len(sortedOods) - i)
    
    if amountPerOod > currentOod.Budget:
        currentOod.Amount=currentOod.Budget
    else:
        currentOod.Amount=int(amountPerOod)
        
    print("AmountLeft : "+ str(amountLeft)+ " ... " + str(currentOod), file=sys.stderr)
    amountLeft=amountLeft-int(currentOod.Amount)
		
if amountLeft > 0:
    print("IMPOSSIBLE")
else:
    for i in range(len(sortedOods)):
        print(sortedOods[i].Amount)