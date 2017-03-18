'''moi'''
s=''
for c in input():
    if c.isdigit(): s+= ''.join(map(chr, range(ord('0'), ord(c)+1)))
    else :
        if c.islower() : s+=''.join(map(chr, range(ord('a'), ord(c)+1)))
        else : s+=''.join(map(chr, range(ord('A'), ord(c)+1)))
print(s)

'''autre'''
a=input()
ans = ""
for i in a:
    if i.isdigit():
        for j in range(int(i)+1):
            ans += chr(ord('0')+j)
    elif i.isupper():
        for j in range(ord(i)-ord('A')+1):
            ans += chr(ord('A')+j)
    elif i.islower():
        for j in range(ord(i)-ord('a')+1):
            ans += chr(ord('a')+j)
print(ans)
