'''1)'''
n=int(input())
w=input()
for i in range(n):w=w[1:]+w[0]
print(w)

'''2)'''
n=int(input())
w=input()
for i,c in enumerate(w):
 print(w[(i+n)%len(w)],end="")

'''3)'''
n=int(input());w=input();s=(w[n:]+w[:n])if n<=len(w) else(w[n%len(w):]+w[:n%len(w)]);print(s)

'''
https://www.codingame.com/clashofcode/clash/report/301538a112786b035c9e98e63447a393a84817
'''
