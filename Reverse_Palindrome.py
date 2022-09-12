def palin(n):
    r=0
    while(n):
        d=n%10
        r=r*10+d
        n//=10
    return r
        
n=int(input())
while(n):
    n=n+palin(n)
    if n==palin(n):
        print(n)
        break
    