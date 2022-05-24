import math
n=int(input())
l=[]
arr=list(map(int,input().split()))[:n]
for i in arr:
    l.append(i*i)
    l.sort()
print(*l)
    