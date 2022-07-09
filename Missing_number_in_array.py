n=int(input())
for i in range(n):
    a=int(input())
    m=list(map(int,input().split()))
    l=[]
    for j in range(1,a+1):
        l.append(j)
    for k in l:
        if k not in m:
            print(k)