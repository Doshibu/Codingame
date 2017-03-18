'''
https://www.codingame.com/clashofcode/clash/report/304647086e3a28b5a60e9089d142218716d692
1)'''
def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

n = int(input())
print(sum(primes(n)))


'''2)'''
n = int(input())
l = 0

while n != 1 :
    for i in range (2, 15000):
        if (n/i).is_integer():
            l += i
            break
    n = n/i
    
print(int(l))

