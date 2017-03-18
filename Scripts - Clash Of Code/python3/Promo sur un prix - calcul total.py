'''s=int(input())
p=int(input())
l=[int(s) for s in range(p)]'''
s=20, p=3, l=[100, 400, 200]
l=l.sort()
print(sum(l[:len(l)]) + max(l)-(l.max()*(s/100)))
