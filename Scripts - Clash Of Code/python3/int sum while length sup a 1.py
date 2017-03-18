n = [int(i) for i in "215"]
while len(str(n)) > 1 :
    n = (sum([int(i) for i in str(sum(n))]))
print(n)
