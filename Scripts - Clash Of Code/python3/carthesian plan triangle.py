g=lambda q,w,e,r,t,u:(q-t)*(r-u)-(e-t)*(w-u)
def p(x,y,q,w,e,r,t,u):
    a=g(x,y,q,w,e,r)<0
    b=g(x,y,e,r,t,u)<0
    c=g(x,y,t,u,q,w)<0
    return(a==b and b==c)
i=lambda:map(int,input().split())
x,y=i()
n=int(input())
for _ in range(n):
    q,w,e,r,t,u=i()
    print('inside' if p(x,y,q,w,e,r,t,u) else 'outside')
