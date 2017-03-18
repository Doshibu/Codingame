input()
T=[int(s) for s in input().split()]
print(T and sorted(sorted(T,reverse=True),key=abs)[0] or 0)
