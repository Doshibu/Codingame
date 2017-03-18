n = 4
l=["1 1 1 1","1 2 3 1","1 2 3 1","1 1 1 1"]
c=0
for i in range(n):
    line = l[i].split(' ')
    if i==0 or i==n-1 :
        c+=sum(list(map(int, line)))-(int(line[0])+int(line[n-1]))
    for y in range(len(line)):
        if y==0 or y==n-1 : 
            c+=int(line[y])
print(c)
